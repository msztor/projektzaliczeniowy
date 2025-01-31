from django.shortcuts import render
from django.http import Http404, HttpResponse

from .models import Produkt

def welcome_view(request):
    
    html = f"""
        <html><body>
        Strona główna </br>
        </body></html>"""
    return HttpResponse(html)

def product_list(request):
    
    produkty = Produkt.objects.all()

    return render(request,
                  "shop/product/list.html",
                  {'produkty': produkty})

def product_detail(request, id):
    # pobieramy konkretny obiekt Person
    try:
        product = Produkt.objects.get(id=id)
    except Produkt.DoesNotExist:
        raise Http404("Obiekt Person o podanym id nie istnieje")

    return render(request,
                  "shop/product/detail.html",
                  {'product': product})