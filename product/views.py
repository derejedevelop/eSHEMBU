from django.shortcuts import render
from .models import productsForSell

# Create your views here.


def addProducts(request):
    return render(request, "addProducts.html")


def productSearch(request):
    prod = productsForSell.objects.all()
    prodName = request.POST['productName']
    return render(request, "mainPage.html", {'product': prod, 'proName': prodName})



