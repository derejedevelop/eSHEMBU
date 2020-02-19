from django.urls import path
from . import views


# home view is added to the url pattern
urlpatterns = [

    path('', views.home, name="home")
]