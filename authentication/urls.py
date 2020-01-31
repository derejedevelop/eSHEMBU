from django.urls import path


from . import views
urlpatterns = [
    path('userAccount', views.userAccount, name="userAccount"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),

]
