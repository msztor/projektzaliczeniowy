from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
import datetime
from django.shortcuts import render
from .models import Product

def welcome_view(request):
    
    html = f"""
        <html><body>
        Home page </br>
        </body></html>"""
    return HttpResponse(html)

def product_list(request):
    
    products = Product.objects.all()

    return render(request,
                  "shop/product/list.html",
                  {'products': products})