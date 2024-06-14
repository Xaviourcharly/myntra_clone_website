from django.db import models
from django.contrib.auth.models import User,AbstractUser

# Create your models here.

class Posts(models.Model):
    name=models.CharField(max_length=30,null=True,blank=True)
    description=models.CharField(max_length=1000,null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    photo=models.ImageField(upload_to='photos')

    def __str__(self):
        return self.name

class Categories(models.Model):
    name=models.CharField(max_length=30,null=True,blank=True)
    description=models.CharField(max_length=1000,null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    photo=models.ImageField(upload_to='photos')

class bohoocatg(models.Model):
    name=models.CharField(max_length=30,null=True,blank=True)
    description=models.CharField(max_length=1000,null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    photo=models.ImageField(upload_to='photos')

    def __str__(self):
        return self.description

class bohoodet(models.Model):
    name=models.CharField(max_length=30,null=True,blank=True)
    description=models.CharField(max_length=1000,null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    photo=models.ImageField(upload_to='photos')

class ShoppingBag(models.Model):
    item=models.ForeignKey(Posts,on_delete=models.CASCADE)



# class Master(models.Model):
#     created_user=models.ForeignKey(Users,on_delete=models.CASCADE)
#     created_data=models.DateField(auto_now_add=True)
#     is_active=models.BooleanField(default=True,verbose_name='Active')




