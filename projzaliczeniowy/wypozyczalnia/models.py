from django.db import models

# Create your models here.

# propozycje modeli:
# Klient, Produkt, Cena, Termin, Zamowienie

from django.db import models

class Klient(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Sprzet(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Cena(models.Model):
    sprzet = models.ForeignKey(Sprzet, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=7)

    def __str__(self):
        return f"Cena dla {self.sprzet.name}: {self.price} PLN"

class Termin(models.Model):
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    sprzet = models.ForeignKey(Sprzet, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"Termin dla {self.klient.firstname} {self.klient.lastname} na {self.sprzet.name} w dniu {self.date}"

class Zamowienie(models.Model):
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    sprzet = models.ForeignKey(Sprzet, on_delete=models.CASCADE)
    cena = models.ForeignKey(Cena, on_delete=models.CASCADE)
    termin = models.ForeignKey(Termin, on_delete=models.CASCADE)
    date_zamowienia = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Zamówienie dla {self.klient.firstname} {self.klient.lastname} na {self.sprzet.name} - {self.date_zamowienia}"

class ZamowienieProdukty(models.Model):
    zamowienie = models.ForeignKey(Zamowienie, on_delete=models.CASCADE)
    product = models.ForeignKey(Sprzet, on_delete=models.CASCADE)  # Zmienione na Sprzet
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    
    class Meta:
        unique_together = (('zamowienie', 'product'),)  # Zmienione na odpowiednie pole

class Produkt(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=7)

    def __str__(self):
        return self.name
    
   
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

