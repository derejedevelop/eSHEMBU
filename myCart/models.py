from django.db import models

# Create your models here.


class myCart(models.Model):
    userId = models.IntegerField()
    productId = models.IntegerField()
    numberOfItems = models.IntegerField(default=1)

