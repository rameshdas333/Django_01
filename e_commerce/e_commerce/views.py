from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# from django.contrib.auth.decorators import login_required
from product.models import Product

# Create your views here.

# @login_required
def home_page(request):
     Context = {}
     product_obj = Product.objects.filter(discount_price__gt=0)
     Context["discounted_product"] = product_obj
     Product.objects.create()
     print(Context)
     return render(request,'pages/index.html',Context)


