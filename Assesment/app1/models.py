from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Items(models.Model):
    id = models.IntegerField(primary_key=True,null=False)
    name = models.CharField(max_length=50,null=False)
    price = models.CharField(max_length=20,null=False)
    description = models.CharField(max_length=200, blank=True)

class Buy_Item(models.Model):
    id = models.IntegerField(primary_key=True,null=False)
    name = models.CharField(max_length=50,null=False)
    price = models.CharField(max_length=20,null=False)
    user  = models.ForeignKey(User, on_delete=models.CASCADE,related_name='buyitem')
    shipping_address= models.CharField(max_length=500)
    contact = models.TextField(max_length=10)