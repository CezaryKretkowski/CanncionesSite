from django.shortcuts import render
from django.views import View
from .LoginForm import LoginForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser



class Login(View):
    template_name = "store/Login.html"
    form_class = LoginForm

    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            user = authenticate(request,username=email,password=password)
            if user is not None:
                login(request,user)
                print(user.is_active)
                redeirect=request.GET.get("redirected_to")
                if redeirect is None:
                    return HttpResponseRedirect("/userview")
                else:   
                    return HttpResponseRedirect(redeirect)
            else:
                form=self.form_class
                return render(request, 'store/LoginValid.html',{'form':form}) 
        else:
            form=self.form_class
            return render(request, 'store/LoginValid.html',{'form':form})
    

    def get(self, request, **kwargs):
        form=self.form_class
        return render(request,self.template_name,{'form':form})