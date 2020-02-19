from django.db import models


# payment model with five parameters
class payment(models.Model):
    fullNameOnCard = models.CharField(max_length=50)
    cardNumber = models.IntegerField()
    cvvNumber = models.IntegerField()
    expDate = models.DateField()
    userId = models.IntegerField()
