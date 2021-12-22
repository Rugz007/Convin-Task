from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)

class Account(models.Model):
    name = models.CharField(max_length=100)

class Contact(models.Model):
    name = models.CharField(max_length=100)
