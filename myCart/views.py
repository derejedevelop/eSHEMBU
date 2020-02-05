from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from product.models import productsForSell
from myCart.models import myCart
from django.contrib import messages
from product.models import productsForSell
from django.views.generic.edit import DeleteView
from .models import myCart



# Create your views here.
def addToCart(request):
    if request.method == 'POST':
        prodId = int(request.POST['prodId'])
        userId = int(request.POST['userId'])
        numItem = 1

        if myCart.objects.filter(userId=userId, productId=prodId).exists():
            messages.info(request, 'Item Already added to Cart')
            prodSell = productsForSell.objects.all()
            cartObj = myCart.objects.all()

            return render(request, 'myCart.html', {'cartObj': cartObj, 'prodSell': prodSell, 'userId': userId,
                                                   'prodId': prodId})
        else:
            item = myCart(userId=userId, productId=prodId, numberOfItems=numItem)
            item.save()
            prodSell = productsForSell.objects.all()
            cartObj = myCart.objects.all()
            return render(request, "myCart.html", {'cartObj': cartObj, 'prodSell': prodSell, 'userId': userId,
                                                   'prodId': prodId})


def displayCart(request):
    if request.method == 'POST':
        print(request.POST['userId'])
        usId = request.POST['userId']
        userId = int(usId)
        print(userId)
        prodSell = productsForSell.objects.all()
        cartObj = myCart.objects.all()

        return render(request, "myCart.html", {'cartObj': cartObj, 'prodSell': prodSell, 'userId': userId})


def deleteFromCart(request):
    if request.method == 'POST':
        print("I am inside delete")
        prodId = int(request.POST['prodId'])
        userId = int(request.POST['userId'])

        myCart.objects.filter(userId=userId, productId=prodId).delete()
        prodSell = productsForSell.objects.all()
        newCartObj = myCart.objects.all()
        return render(request, "myCart.html", {'cartObj': newCartObj, 'prodSell': prodSell, 'userId': userId})



