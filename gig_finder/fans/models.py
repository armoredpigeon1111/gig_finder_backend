from django.db import models

# Create your models here.

class Fan(models.Model):
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    genre1 = models.CharField(max_length=50)
    genre2 = models.CharField(max_length=50)
    genre3 = models.CharField(max_length=50)