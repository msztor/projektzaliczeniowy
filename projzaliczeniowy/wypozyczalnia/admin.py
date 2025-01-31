from django.contrib import admin
from .models import Klient, Termin, Produkt, Cena, Zamowienie, ZamowienieProdukty, Category


class ProduktAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'price', 'description']

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'lastname', 'role'] 

# Register your models here.
admin.site.register(Klient)
admin.site.register(Termin)
admin.site.register(Cena)
admin.site.register(ZamowienieProdukty)
admin.site.register(Produkt, ProduktAdmin)
admin.site.register(Zamowienie)
admin.site.register(Category)
