from product.models import Product
from django.http import JsonResponse

def product_api(request):
    limit = int(request.GET.get('limit', 1))
    offset = int(request.GET.get('offset', 0))
    search = request.GET.get('search')
    print(limit,"RRRRRRRR1")
    print(offset,"RRRRR2")
    print(search)

    products = Product.objects.all()
    
    if search:
        products = products.filter(name__icontains=search)
        
    start = offset
    end = offset + limit
    new_data = products[start:end]
    
    products = list(new_data.values("name"))
    
    return JsonResponse({
        "data":products
    })