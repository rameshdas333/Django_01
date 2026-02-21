from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

def sign_up(request):
    if request.method == "POST":
        data = request.POST
        name = data.get('name',"default")
        email = data.get('email',"default")
        print(request.POST)
        return render(request,'pages/signup.html')