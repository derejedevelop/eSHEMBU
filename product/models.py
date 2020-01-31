from django.db import models

# Create your models here.


class productsForSell(models.Model):
    productName = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    image1 = models.ImageField(upload_to="productImages", height_field=None,
                               max_length=None, width_field=None, blank=True)
    image2 = models.ImageField(upload_to="productImages", height_field=None,
                               max_length=None, width_field=None, blank=True)
    image3 = models.ImageField(upload_to="productImages", height_field=None,
                               max_length=None, width_field=None, blank=True)
    image4 = models.ImageField(upload_to="productImages", height_field=None,
                               max_length=None, width_field=None, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=3, blank=True)
    amountInStock = models.IntegerField()
    rating = models.IntegerField()
    packageWeight = models.DecimalField(max_digits=6, decimal_places=3)
