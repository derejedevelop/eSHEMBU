from django.shortcuts import render
from product.models import productsForSell
from django.contrib.auth.models import User, auth


# home function triggers the first user view
def home(request):
    counter = 1
    prodCol1 = []
    prodCol2 = []

    # all products in ProductsForSell added to two lists
    for i in productsForSell.objects.all():
        if counter % 2 == 1:
            prodCol1.append(i)
        else:
            prodCol2.append(i)
        counter += 1

    # the two list are added to one object zipped
    product = zip(prodCol1, prodCol2)

    # render the index.html page and send product object to the template
    if request.method == 'POST':
        # prod = productsForSell.objects.all()
        return render(request, 'index.html', {'product': product})
    else:
        # prod = productsForSell.objects.all()
        return render(request, 'index.html', {'product': product})