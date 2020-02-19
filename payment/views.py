from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import payment
# Create your views here.


# takes users payment information and save it in the database
def addPayment(request):
    if request.method == 'POST':
        userId1 = request.POST['userId']
        ret = request.POST['ret']

        if userId1 is not None and ret == 'no':
            return render(request, 'addPayment.html', {'userId': userId1})
        else:
            # takes user information
            fullNameOnCard = request.POST['fullNameOnCard']
            cardNumber = request.POST['cardNumber']
            cvvNumber = request.POST['cvvNumber']
            expDate = request.POST['expDate']

            # create a payment object
            paymentInfo = payment(fullNameOnCard=fullNameOnCard, cardNumber=cardNumber, cvvNumber=cvvNumber,
                                  expDate=expDate, userId=userId1)
            # save the object to the database
            paymentInfo.save()
    # redirect to the home page
    return redirect("/")






