from django.db import models

# Create your models here.

# propozycje modeli:
#  Employee, Product, Category, Customer, Order

class RoleType(models.TextChoices):
    Sales = 'Sales'
    Marketing = 'Marketing'

class Employee(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    role = models.CharField(max_length=50, choices=RoleType.choices)
    age = models.PositiveIntegerField()

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

class Product(models.Model):
    price =models.DecimalField(decimal_places=2, max_digits=7)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    

class Customer(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Order(models.Model):
    number = models.IntegerField(primary_key=True)
    date_created =models.DateField(auto_now=True)
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class OrderProducts(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product =models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(decimal_places=2, max_digits=7)

    class Meta:
        unique_together = (('order', 'product'),)

   

