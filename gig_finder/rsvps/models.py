from django.db import models

# Create your models here.

class RSVP(models.Model):
    gig = models.ForeignKey('gigs.Gig', on_delete=models.CASCADE)
    fan = models.ForeignKey('fans.Fan', on_delete=models.CASCADE)