from django.urls import path
from .api import *
from  .views import *

urlpatterns = [
    path('check-duplicate',duplicate_check, name='check_duplicate')
   
]