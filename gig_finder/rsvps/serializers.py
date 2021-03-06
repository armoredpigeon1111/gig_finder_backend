from rest_framework import serializers
from .models import RSVP


class RSVPSerializer(serializers.ModelSerializer):
    class Meta:
        model = RSVP
        fields = ['id', 'fan', 'gig']