from django.urls import path


from . import views
urlpatterns = [

    path('addProducts', views.addProducts, name="addProducts"),
    path('productSearch', views.productSearch, name="productSearch"),

]
