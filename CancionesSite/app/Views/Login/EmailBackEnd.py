from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from ...Entities.Users.User import User

class EmailBackEnd(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            print(username)
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            print("done1")
            return None
        
        else:
            print("done02")
            if user.check_password(password):
                print("done2")
                user.is_active=True
                user.save()
                return user
        return None