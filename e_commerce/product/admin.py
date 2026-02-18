from django.contrib import admin
from .models import Product,Category,Color,Inventory

class ProductAdmin(admin.ModelAdmin):
    list_display =('name','in_stock')


admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Inventory)

# Register your models here.
