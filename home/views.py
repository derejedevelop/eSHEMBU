from django.shortcuts import render
from product.models import productsForSell

# Create your views here.


def home(request):
    prod = productsForSell.objects.all()
    return render(request, 'index.html', {'product': prod})