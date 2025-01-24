from django.contrib import admin
from .models import Customer, Category, Order, OrderProducts, Employee, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'price', 'description']

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'lastname', 'role'] 

# Register your models here.
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderProducts)
admin.site.register(Product, ProductAdmin)
