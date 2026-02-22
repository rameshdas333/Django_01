# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views import View
# from django.contrib import messages


# # Create your views here.

# def sign_up(request):
#     if request.method == "POST":
#         data = request.POST
        
#         name = data.get('name',"")
#         email = data.get('email',"")
#         password = data.get('password',"")
#         confirm_password = data.get('confirm_password',"")
#         if password != confirm_password:
#             messages.success(request,"Confirm password is not same as password")
#             return render(request,'pages/signup.html')
#     messages.objects.create(full_name=name,email=email,password=password, confirm_password=password)
      
#     return render(request,'pages/signup.html')

from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

def sign_up(request):
    if request.method == "POST":
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        password = request.POST.get('password', "")
        confirm_password = request.POST.get('confirm_password', "")

        if password != confirm_password:
            messages.error(request, "Confirm password is not same as password")
            return render(request, 'pages/signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return render(request, 'pages/signup.html')

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password
        )
        user.first_name = name
        user.save()

        messages.success(request, "Account created successfully")
        return render(request, 'pages/signup.html')

    return render(request, 'pages/signup.html')