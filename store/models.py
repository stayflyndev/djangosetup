from django.db import models
import datetime
# Create your models here.
# Create Classes for tables to SQL

#Products
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self): 
        return self.name
    
#Customer Information
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self): 
        return f'{self.first_name} {self.last_name}'

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50, default ="", blank=True, null=True )
    image = models.ImageField(upload_to="uploads/product/")
    price = models.DecimalField(default=0, decimal_places=2, max_digits=5)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    def __str__(self): 
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product,  on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,)
    quantity = models.IntegerField(default=1)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    def __str__(self): 
        return self.product