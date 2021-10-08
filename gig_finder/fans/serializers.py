from rest_framework import serializers
from .models import Fan


class FanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fan
        # fields = ['id', 'genre1', 'genre2', 'genre3', 'user_id']
        fields = ['id', 'genre1', 'genre2', 'genre3', 'user']