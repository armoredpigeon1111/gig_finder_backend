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

    # permission_classes = [AllowAny]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        musicians = Musician.objects.all()
        serializer = MusicianSerializer(musicians, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MusicianSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class MusicianIndividual(APIView):
    def get(self, request, user_id):
        musician = Musician.objects.filter(user_id = user_id)
        serializer = MusicianSerializer(musician, many=True)
        return Response(serializer.data)