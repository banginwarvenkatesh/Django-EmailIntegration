from django.db import models

class User(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    email=models.EmailField()


# Create your models here.
