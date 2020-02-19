from django.urls import path


from . import views
urlpatterns = [
    path('addPayment', views.addPayment, name="addPayment"),
]