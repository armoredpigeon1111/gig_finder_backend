from django.db import models

# Create your models here.

class Review(models.Model):
    gig = models.ForeignKey('gigs.Gig', blank=True, null=True, on_delete=models.CASCADE)
    body = models.CharField(max_length=500)