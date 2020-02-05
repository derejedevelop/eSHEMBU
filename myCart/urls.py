from django.urls import path


from . import views
urlpatterns = [

    path('addToCart', views.addToCart, name="addToCart"),
    path('displayCart', views.displayCart, name="displayCart"),
    path('deleteFromCart', views.deleteFromCart, name="deleteFromCart"),

]