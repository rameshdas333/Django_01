
from django.urls import path, include
from  .views import *
from .api import *
from rest_framework.routers import DefaultRouter
routers = DefaultRouter()
# routers.register('rest-api',ProductViewset,basename='product-api')


urlpatterns = [
    path('',include(routers.urls)),
    path('',product_page,name="product_page"),
    path('api/',product_api,name="product_api")
    # path('home/', home, name='home'),
    # path('home_class/',HomeView.as_view (), name='home'),
]