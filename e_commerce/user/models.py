from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission
from django.utils.translation import gettext_lazy as _


GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]


class User(AbstractUser):
    first_name = None
    last_name = None
    full_name = models.CharField(max_length=255,blank=True,null=True)
    phone_number = models.CharField(max_length=255,blank=True,null=True)
    gender = models.CharField(
        max_length=6,
        choices=GENDER_CHOICES,
        blank=True,
        null=True
    )
    # groups = models.ManyToManyField(
    # Group,
    #     verbose_name=_("groups"),
    #     blank=True,
    #     related_name="user_set1",
    #     related_query_name="user1",
    # )
    # user_permissions = models.ManyToManyField(
    #     Permission,
    #     blank=True,
    #     related_name="user_set1",
    #     related_query_name="user1",
    # )
    
    

# Create your models here.
# class Profile(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     phone_number = models.CharField(max_length=225,blank=True,null=True)

