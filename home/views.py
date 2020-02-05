from django.shortcuts import render
from product.models import productsForSell
from django.contrib.auth.models import User, auth

# Create your views here.


def home(request):
    prod = productsForSell.objects.all()

    return render(request, 'index.html', {'product': prod})