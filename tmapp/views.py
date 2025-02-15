from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
# from .models import Feature

def index(request): 

    return render(request, 'index.html')

def login(request): 

    return render(request, 'login.html')

def registration(request): 
    if request.method == 'POST':
        username = request.POST['username']
        last_name = request.POST['last_name']
        email = request.POST['corporate_email']
        phone_number = request.POST['phone_number']
        registration_number = request.POST['registration_number']
        dob = request.POST['dob']
        password = request.POST['password']
        password2 = request.POST['password2']
        remember = request.POST['remember']

        if password == password2:
            if User.objects.filter(email = email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('registration')
            # elif User.objects.filter(registration_number = registration_number).exists():
            #     messages.info(request, 'Registration Number Already Used')
            #     return redirect('registration') 
            else:
                user = User.objects.create_user(username=username, last_name=last_name, corporate_email=email, phone_number=phone_number, registration_number=registration_number, dob=dob, password=password, remember= remember)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Password Not The Same')
            return redirect('registration') 
    else:
        return render(request, 'registration.html')

    
# def register(request): 
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         password2 = request.POST['password2']

#         if password == password2:
#             if User.objects.filter(email = email).exists():
#                 messages.info(request, 'Email Already Used')
#                 return redirect('register')
#             elif User.objects.filter(username = username).exists():
#                 messages.info(request, 'Username Already Used')
#                 return redirect('register') 
#             else:
#                 user = User.objects.create_user(username=username, email=email, password=password)
#                 user.save();
#                 return redirect('login')
#         else:
#             messages.info(request, 'Password Not The Same')
#             return redirect('register') 
#     else:
#         return render(request, 'register.html')
    
# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password'] 
#         user =auth.authenticate(username=username, password=password)

#         if user is not None:
#             auth.login(request, user)
#             return redirect('/') #homepage
#         else:
#             messages.info(request, 'Credentials Invalid')
#             return redirect('login')
#     else:
#         return render(request, 'login.html')
    
def logout(request):
    auth.logout(request) 

    return redirect('/')

def verify(request): 

    return render(request, 'verify.html')

def memb_dash(request): 

    return render(request, 'memb_dash.html')
def memb_roles(request): 

    return render(request, 'memb_roles.html')

