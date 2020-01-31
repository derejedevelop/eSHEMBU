from django.db import models

# Create your models here.


class userAccount(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    userName = models.CharField(max_length=100, default="dereje")
    passWord = models.CharField(max_length=100)
    email = models.EmailField()
    phoneNumber = models.IntegerField()