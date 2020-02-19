from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from product.models import productsForSell
from myCart.models import myCart
from django.contrib import messages
from product.models import productsForSell
from django.views.generic.edit import DeleteView
from .models import myCart


# adds products to the cart
def addToCart(request):

    # if request is POST
    if request.method == 'POST':
        prodId = int(request.POST['prodId'])
        userId = int(request.POST['userId'])
        numItem = int(request.POST['Qty'])
        cartEmpty = False

        # checks if the userId and ProductId exist in one row in myCart database
        if myCart.objects.filter(userId=userId, productId=prodId).exists():
            # If it exists it send a message
            messages.info(request, 'Item Already added to Cart')
            prodSell = productsForSell.objects.all()
            cartObj = myCart.objects.all()

            # render to myCart.html page passing two objects, two string, and one boolean
            return render(request, 'myCart.html', {'cartObj': cartObj, 'prodSell': prodSell, 'userId': userId,
                                                   'prodId': prodId, 'cartEmpty': cartEmpty})
        else:
            # if item does not exist it will be added to myCart database
            item = myCart(userId=userId, productId=prodId, numberOfItems=numItem)
            item.save()
            prodSell = productsForSell.objects.all()
            cartObj = myCart.objects.all()

            # render to myCart.html page passing two objects, two string, and one boolean
            return render(request, "myCart.html", {'cartObj': cartObj, 'prodSell': prodSell, 'userId': userId,
                                                   'prodId': prodId, 'cartEmpty': cartEmpty})


# displays what is in the cart for a specific customer
def displayCart(request):

    if request.method == 'POST':
        usId = request.POST['userId']
        userId = int(usId)

        prodSell = productsForSell.objects.all()
        cartObj = myCart.objects.all()

        # checks if the cart is empty or not
        if myCart.objects.filter(userId=usId).exists():
            cartEmpty = False
        else:
            cartEmpty = True

        # render to myCart.html page passing two objects, two string, and one boolean
        return render(request, "myCart.html", {'cartObj': cartObj, 'prodSell': prodSell, 'userId': userId,
                                               'cartEmpty': cartEmpty})


# deletes products which are already added to the cart
def deleteFromCart(request):
    if request.method == 'POST':
        prodId = int(request.POST['prodId'])
        userId = int(request.POST['userId'])

        # delete selected product from myCart database
        myCart.objects.filter(userId=userId, productId=prodId).delete()
        prodSell = productsForSell.objects.all()
        newCartObj = myCart.objects.all()

        # check if the cart is empty or not
        if myCart.objects.filter(userId=userId).exists():
            cartEmpty = False
        else:
            cartEmpty = True

        # render to myCart.html page passing two objects, two string, and one boolean
        return render(request, "myCart.html", {'cartObj': newCartObj, 'prodSell': prodSell, 'userId': userId,
                                               'cartEmpty': cartEmpty})





