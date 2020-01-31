from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from product.models import productsForSell

# Create your views here.


def logout(request):
    auth.logout(request)
    return redirect("/")


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            # if username == 'dereje':
            #     return redirect('addProducts')
            # else:
            prod = productsForSell.objects.all()
            return render(request, 'mainPage.html', {'product': prod})
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def userAccount(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "User name taken")
                return redirect('userAccount')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email taken")
                return redirect('userAccount')
            else:
                user = User.objects.create_user(username=username, password=password1, first_name=first_name,
                                        last_name=last_name, email=email)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Password does not match")
            return redirect('userAccount')

        return redirect('login')
    else:
        return render(request, 'createAccount.html')


