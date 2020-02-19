from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from product.models import productsForSell
from authentication.models import userAccount


# Create your views here.
# logout function logs out users
def logout(request):
    if request.method == 'POST':
        # authenticated user will be logged out of the app
        auth.logout(request)
        return redirect("/")


# login function logs in users
def login(request):

    # checks if there is a POST request
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        userObj = auth.models.User.objects.all()

        # checks if a user with entered user name and password exists on the database
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            prod = productsForSell.objects.all()
            request.session.set_expiry(0)

            # if user exists it renders the main page.
            return render(request, 'mainPage.html', {'product': prod, 'user': user})
        else:

            # sends a message and lets user try to login again.
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        # if no POST request it renders a login page again.
        return render(request, 'login.html')


# enables new users create their account
def userAccount(request):

    if request.method == 'POST':

        # accepts five values from users
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # checks if first and second password entered are the same
        if password1 == password2:
            # checks if the user name exists on the database
            if User.objects.filter(username=username).exists():
                # if user exists sends message and redirect to account create page
                messages.info(request, "User name taken")
                return redirect('userAccount')
            # checks if entered email already exists on the databasa
            elif User.objects.filter(email=email).exists():
                # if email exists, sends message and redirect to account create page
                messages.info(request, "Email taken")
                return redirect('userAccount')
            else:
                # saves all information entered to the system.
                user = User.objects.create_user(username=username, password=password1, first_name=first_name,
                                        last_name=last_name, email=email)
                user.save()
                return redirect('login')
        else:
            # if both passwords does not match, redirect to account creation page.
            messages.info(request, "Password does not match")
            return redirect('userAccount')

        return redirect('login')
    else:
        return render(request, 'createAccount.html')


