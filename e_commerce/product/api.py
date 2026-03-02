from product.models import Product
from django.http import JsonResponse
from rest_framework import viewsets,generics
from product.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

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
    
    
class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        print(queryset)
        return Response("called")


@api_view(["GET","DELETE"])
def product_api_function(request):
    if request.method == "GET":
        product = Product.objects.get(id=5)
        serializer = ProductSerializer(product,many=False) 
        print(product)
        print(serializer)
        print(serializer.data)
        return Response(serializer.data)
    
   
class ProductViewset(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer()