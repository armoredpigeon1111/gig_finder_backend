from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Gig
from .serializers import GigSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

class GigList(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        gigs = Gig.objects.all()
        serializer = GigSerializer(gigs, many=True)
        return Response(serializer.data)