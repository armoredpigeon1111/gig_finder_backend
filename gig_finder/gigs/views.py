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

    # permission_classes = [AllowAny]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        gigs = Gig.objects.all()
        serializer = GigSerializer(gigs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GigSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)        

class GigIndividual(APIView):
    def get(self, request, pk):
        gig = Gig.objects.filter(pk = pk)
        serializer = GigSerializer(gig, many=True)
        return Response(serializer.data)