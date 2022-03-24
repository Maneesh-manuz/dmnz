from email.policy import default
from django.db import models

# Create your models here.


class items(models.Model):
    modelname = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    gib = models.ImageField(default="default.png", upload_to="images")
    price = models.CharField(max_length=255)
    types = models.CharField(max_length=255)
    format = models.CharField(max_length=255)
    modeltype = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    fbx = models.ImageField(default="default.png", upload_to="images")


class payment(models.Model):
    modelname = models.ForeignKey(items,on_delete=models.DO_NOTHING , related_name='pay_model',null=True,blank=True)
    price = models.ForeignKey(items , on_delete=models.DO_NOTHING , related_name='pay_price',null=True,blank=True)
    clientname = models.CharField(max_length=225 ,null=True)
    date=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True) 
   
