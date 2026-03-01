from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from product.models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def product_page(request):
    Context = {}
    product_obj = Product.objects.filter()
    Context["products"] = product_obj
    return render(request,'pages/product.html',Context)



# def home(request):
#     print(request.method)
#     print(request.user)
#     return HttpResponse("<h1>Hello World New!</h1>")
# class HomeView(View):
#  def get(self,request):
#          return HttpResponse("<h1>Hello World New Ramesh!</h1>")
