from django.db import models

# Create your models here.


class Admin_Login(models.Model):
    a_username=models.CharField(max_length=20)
    a_password=models.CharField(max_length=20)

class Upload_Product(models.Model):
    product_category=models.CharField(max_length=10)
    product_name=models.CharField(max_length=20)
    product_brand=models.CharField(max_length=20)
    product_price=models.DecimalField(max_digits=10,decimal_places=2)
    upload_image=models.ImageField(upload_to='loki/')

class User_Login(models.Model):
    u_username=models.CharField(max_length=20)
    u_password=models.CharField(max_length=20)
    email=models.EmailField(primary_key=True)

class user_Orders(models.Model):
    product_name = models.CharField(max_length=20)
    product_brand = models.CharField(max_length=20)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    upload_image = models.ImageField(upload_to='orders/')
    email_id = models.EmailField(primary_key=True)


class Comments(models.Model):
    name=models.CharField(max_length=20)
    comment=models.TextField()
    rate=models.IntegerField()
    email=models.EmailField()

