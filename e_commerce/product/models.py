

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
      

import os

#product ar name a  image pawer jonno 

def upload_image_path(instance, filename):
    extension = filename.rsplit('.', 1)[-1]
    filename = f"{instance.name}_{instance.product_code}.{extension}"
    return os.path.join("products", filename)
#========================

class Product(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    product_code= models.CharField(max_length=255,null=True,blank=True)
    # category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    color = models.ManyToManyField(Color,blank=True)
    image = ResizedImageField(size=[500,300],quality=75, upload_to=upload_image_path, null=True, blank=True) #force_format="png"

    discount_price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    retail_price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    in_stock = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.name) or "" #f"{self.name}"
    
    
    @property
    def discount_parcentage(self):
        if self.discount_price > 0:
            diff = self.discount_price - self.retail_price
            parcent = (diff/self.retail_price) * 100
            
            return round(parcent,2)
        return 0
        
def save(self, *args, **kwargs):
    name = self.image.name
    extension = name.split('.')[-1]
    new_name = f"{self.name}_{self.product_code}.{extension}"

    print(name)
    print(extension)
    print(new_name) 
    self.image.name =new_name
    super().save(*args, **kwargs)
    
class Inventory(models.Model):
         product = models.OneToOneField(Product,on_delete=models.CASCADE,null=True,blank=True )
         quantity= models.PositiveIntegerField(default=0)
         def __str__(self):
            return f"{self.product} - {self.quantity}"
