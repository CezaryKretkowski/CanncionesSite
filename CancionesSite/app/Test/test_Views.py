from django.test import RequestFactory,TestCase
from django.contrib.sessions.middleware import SessionMiddleware
from django.urls import reverse
from ..Views.User.UserView import UserView
from ..Entities.Users.User import User
from ..Entities.Users.Address import Address
from ..Entities.Dictionary.Address.City import City
from django.contrib.auth.models import AnonymousUser
from django.test import Client


class TestUserView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.city=City.objects.create(name="city")
        self.addres=Address.objects.create(
            street="street",number=1,
            zipCode="25-895",
            flatNumber=7,
            city=self.city)
        self.user=User.objects.create_user(
            user_name="user",email="user@gmail.com"
            ,password="password",last_name="NoAdmin"
            ,first_name="jackob",address=self.addres)

        
    def test_UserView_get(self):
        request = self.factory.get('userview')
        middleware = SessionMiddleware(request)
        middleware.process_request(request)
        request.session.save()
        request.user = self.user
        
        
        response=UserView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        request.user = AnonymousUser()
        response=UserView.as_view()(request)
        self.assertEqual(response.status_code, 302)
        
    def test_UserView_post(self):
        request = self.factory.post('userview')
        request.data=[{"password":"pass","confirmPassword":'pass'}]
        middleware = SessionMiddleware(request)
        middleware.process_request(request)
        request.session.save()
        request.user = self.user
        response=UserView.as_view()(request)
        self.assertEqual(response.status_code, 200)