from django.urls import path

# all authentication view functions paths are added to the URL
from . import views
urlpatterns = [
    path('userAccount', views.userAccount, name="userAccount"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),

]
