from django.views import View 
from django.shortcuts import render 
from .RegistrationForm import RegistrationForm
from .AddressForm import AddressForm
from ...Entities.Dictionary.Address.City import City
from ...Entities.Users import Address,User 
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

class RegistrationView(View):
    #form_class=
    def get(self, request, *args, **kwargs):
        regForm = RegistrationForm()
        addressForm = AddressForm()
        try:
            cities=City.objects.all()
        except City.DoesNotExist :
            cities=[]
        return render(request,"store/Register.html",{"regForm":regForm,'cities':cities})

    def post(self, request, *args, **kwargs):
        data=request.POST

        cityID=data['city']
        try:
            city=City.objects.get(id=cityID)
        except City.DoesNotExist:
            return HttpResponse("error")
        
        form=RegistrationForm(data)
        if form.is_valid():
            clenData=form.cleaned_data
            try:
                user=User.User.objects.get(email=clenData['email'])
                return HttpResponse("error")
            except User.User.DoesNotExist:
                pass
            try:
                user=User.User.objects.get(user_name=clenData['username'])
                return HttpResponse("error")
            except User.User.DoesNotExist:
                pass
            if clenData['password'] == clenData['confirmPassword']:
                
                addres=Address.Address.objects.create(street=clenData['street'],number=clenData['number'],
                                           zipCode=clenData['zipcode'],
                                           flatNumber=clenData['flat_number'],
                                           city=city)
                user=User.User.objects.create_user(user_name=clenData['username'],email=clenData['email']
                                              ,password=clenData['password'],last_name=clenData['last_name']
                                              ,first_name=clenData['first_name'],address=addres)
                user.is_active=True
                user.save()
                # user = authenticate(request,username=user.email,password=user.password)
                login(request,user)
            else :
                return HttpResponse("wrong valid")
            
            
            
        return HttpResponseRedirect("/userview")