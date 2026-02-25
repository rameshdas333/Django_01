from django.urls import path
from  .views import *
from .api import *

urlpatterns = [
    path('',product_page,name="product_page"),
    path('api/',product_api,name="product_api")
    # path('home/', home, name='home'),
    # path('home_class/',HomeView.as_view (), name='home'),
]