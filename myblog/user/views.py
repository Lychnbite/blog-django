from django.contrib.auth.models import User
from django.shortcuts import render, redirect 
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages



# Create your views here.
from .models import *
from .forms import RegisterForm ,LoginForm



# Create your views here.


def register(request):

    form = RegisterForm(request.POST or None)


    if form.is_valid():
        username  = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username=username)
        newUser.set_password(password)

        newUser.save()
        login(request,newUser)
        messages.success(request,"İşlem başarı ile gerçekleştirildi")
        return redirect("user:login")


    context = {
        "form":form
    }

    return render(request,"user/register.html",context)
    
    

def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username= username, password=password)

        if user is None:
            messages.info(request,"Kullanıcı adı veya parola hatalı")
            return render(request,"user/login.html",context)

        messages.success(request,"Başarı ile giriş yaptınız")
        login(request,user)
        return redirect("article:index")


    return render(request,"user/login.html",context)
    
def logoutUser(request):
    logout(request)
    messages.success(request,"Çıkış Yaptınız")
    return redirect("article:index")




