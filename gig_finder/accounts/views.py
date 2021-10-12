from django.http.response import Http404
from rest_framework import status
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import User
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
User = get_user_model()


class UserIndividual(APIView):  
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        user = User.objects.filter(id = id)
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)