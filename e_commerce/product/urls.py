from django.urls import path
from  .views import *

urlpatterns = [
    path('',product_page,name="product_page")
    # path('home/', home, name='home'),
    # path('home_class/',HomeView.as_view (), name='home'),
]