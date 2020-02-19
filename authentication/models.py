from django.db import models


# Create user account model.
class userAccount(models.Model):
    # model has six parameters
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    userName = models.CharField(max_length=100, default="dereje")
    passWord = models.CharField(max_length=100)
    email = models.EmailField()
    phoneNumber = models.IntegerField()