from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

def sign_up(request):
    
    print(request)
    print(request)
    return render(request,'pages/signup.html')