from django.db import models

# Create your models here.

class RSVP(models.Model):
    gig = models.ForeignKey('gigs.Gig', blank=True, null=True, on_delete=models.CASCADE)
    fan = models.ForeignKey('fans.Fan', blank=True, null=True, on_delete=models.CASCADE)