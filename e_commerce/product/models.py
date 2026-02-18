

from django.db import models

from django_resized import ResizedImageField


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    def __str__(self):
      return self.name
    
class Color(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    def __str__(self):
          return self.name

class Product(models.Model):
  
    name = models.CharField(max_length=255,null=True,blank=True)
    product_code= models.CharField(max_length=255,null=True,blank=True)
    # category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    color = models.ManyToManyField(Color,blank=True)
    image = ResizedImageField(size=[500,300],quality=75, upload_to='products/', null=True, blank=True)

    discount_price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    retail_price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    in_stock = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.name)#f"{self.name}"
    
    
class Inventory(models.Model):
         product = models.OneToOneField(Product,on_delete=models.CASCADE,null=True,blank=True )
         quantity= models.PositiveIntegerField(default=0)
         def __str__(self):
            return f"{self.product} +{self.quantity}"
