from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

def home_page(request):
    return render(request,'pages/home.html')