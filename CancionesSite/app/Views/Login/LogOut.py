from django.shortcuts import render
from django.views import View
from django.contrib.auth import logout
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponseRedirect

class LogOut(View):
    template_name = "store/Logout.html"
    def get(self, request, **kwargs):
        user=request.user
        if isinstance(user,AnonymousUser):
            return HttpResponseRedirect("/login")
        else:
            logout(request)
            return render(request,self.template_name)