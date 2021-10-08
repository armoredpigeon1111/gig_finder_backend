from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Musician
from .serializers import MusicianSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

class MusicianList(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        musicians = Musician.objects.all()
        serializer = MusicianSerializer(musicians, many=True)
        return Response(serializer.data)

class MusicianIndividual(APIView):
    def get(self, request, user_id):
        musician = Musician.objects.filter(user_id = user_id)
        serializer = MusicianSerializer(musician, many=True)
        return Response(serializer.data)