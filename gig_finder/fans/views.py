from rest_framework import status
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Fan
from .serializers import FanSerializer
from django.contrib.auth import get_user_model
User = get_user_model()


class FanList(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        fans = Fan.objects.all()
        serializer = FanSerializer(fans, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FanSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
