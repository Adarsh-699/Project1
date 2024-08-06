from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from . models import *
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def show_account(request):
    context={}
    if request.POST and 'register' in request.POST:
        context['register']=True
        try:
            username=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')
            phone=request.POST.get('phone')
            address=request.POST.get('address')
            # create user
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            #create customer
            customer=Customers.objects.create(
                name=username,
                user = user,
                phone=phone,
                address=address
            )
            success_message="Registration successful."
            messages.success(request,success_message)
            subject = 'Registration Successful'
            message = 'You have successfully created an account in SwiftKart. You can Login to experience the Application'
            recipient = user.email
            send_mail(subject, 
            message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
        except Exception as e:
            error_message="Invalid credentials or Duplicate username found"
            messages.error(request,error_message)
    if request.POST and 'login' in request.POST:
        context['register']=False
        try:
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect('index_page')
            else:
                error_message="Invalid credentials"
                messages.error(request,error_message)
        except Exception as e:
            error_message="Invalid credentials"
            messages.error(request,error_message)
    return render(request,'account.html',context)

def signout(request):
    logout(request)
    return redirect('account')