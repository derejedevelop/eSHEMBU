from django.shortcuts import render
from .models import productsForSell

# Create your views here.


def addProducts(request):
    # returns the addProducts.html

    return render(request, "addProducts.html")


def productSearch(request):
    prod = productsForSell.objects.all()


    # for a in productsForSell.objects.all():
    #     print(productsForSell.productName.name)
    #
    # if request.method == 'POST':
    prodName = request.POST['productName']
    return render(request, "mainPage.html", {'product': prod, 'proName': prodName})