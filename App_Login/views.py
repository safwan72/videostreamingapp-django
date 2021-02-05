from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from App_Login.forms import SignUpForm,ProfileUpdate
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.


def profileupdate(request):
    form=ProfileUpdate(instance=request.user)
    if request.method=='POST':
        form=ProfileUpdate(data=request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            form=ProfileUpdate(instance=request.user)
            messages.info(request,'Profile Updated Succesfully!!!!!')
    dicts={'form':form}
    return render(request,'App_Login/changeProfile.html',context=dicts)


def signupview(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'Account Created Succesfully!!!!!')
            return HttpResponseRedirect(reverse('App_Video:home'))
    dicts={'form':form}
    return render(request,'App_Login/form.html',context=dicts)

def loginview(request):
    form=AuthenticationForm()
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.info(request,f'Login Succesful for {username}')
            return HttpResponseRedirect(reverse('App_Video:home'))
    dicts={'form':form}
    return render(request,'App_Login/Login.html',context=dicts)

@login_required
def logoutview(request):
    logout(request)
    messages.warning(request,'Logged Out Succesfully')
    return HttpResponseRedirect(reverse('App_Video:home'))