from django.db import models

# Create your models here.

class Musician(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    bandName = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
