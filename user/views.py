from django.shortcuts import render,redirect,get_object_or_404
from .forms import SignUpForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout


def signup_view(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password1']
            user=User.objects.create_user(username=username,email=email,password=password)
            return redirect('login_sahifa')

    context={
        'form':form
    }

    return render(request,"registration/signup.html",context)


def login_view(request):
    form=LoginForm()
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('bosh_sahifa')

    context={
        'form':form
    }

    return render(request,"registration/login.html",context)



#saytdan chiqib ketish

def logout_page(request):
    logout(request)
    return redirect('login_sahifa')





def profile_page(request):
    return render(request,"registration/profile.html")





