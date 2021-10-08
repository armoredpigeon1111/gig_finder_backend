from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Review
from .serializers import ReviewSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

class ReviewList(APIView):

    # permission_classes = [AllowAny]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReviewSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)        

class ReviewIndividual(APIView):
    def get(self, request, gig_id):
        review = Review.objects.filter(gig_id = gig_id)
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data)