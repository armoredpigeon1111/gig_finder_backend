from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Gig(models.Model):
    musician = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    likes = models.IntegerField()
