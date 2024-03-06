from django.db import models

# Create your models here.

class Product(models.Model):
    item_name = models.CharField(max_length=100)
    item_price = models.FloatField()
    item_discount_price = models.FloatField()
    item_desc = models.TextField()
    item_image = models.CharField(max_length=500)
    item_category = models.CharField(max_length=100)
    
    
    def __str__(self):
        return f"{self.item_name} is in {self.item_category}"
    
class Order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)
    total = models.CharField(max_length=100, default=0)
   
    def __str__(self):
        return f"{self.name} order details"