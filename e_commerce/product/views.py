from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

def product_page(request):
    return render(request,'pages/product.html')



# def home(request):
#     print(request.method)
#     print(request.user)
#     return HttpResponse("<h1>Hello World New!</h1>")
# class HomeView(View):
#  def get(self,request):
#          return HttpResponse("<h1>Hello World New Ramesh!</h1>")
