from rest_framework import serializers
from .models import Gig


class GigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gig
        fields = ['id', 'street', 'city', 'state', 'zipcode', 'likes', 'musician', 'dateTime']