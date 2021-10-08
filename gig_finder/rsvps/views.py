from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import RSVP
from .serializers import RSVPSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

class RSVPList(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        rsvps = RSVP.objects.all()
        serializer = RSVPSerializer(rsvps, many=True)
        return Response(serializer.data)

class RSVPFan(APIView):
    def get(self, request, fan_id):
        rsvp = RSVP.objects.filter(fan_id = fan_id)
        serializer = RSVPSerializer(rsvp, many=True)
        return Response(serializer.data)