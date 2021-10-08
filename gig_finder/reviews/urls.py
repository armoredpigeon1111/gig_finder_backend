from django.urls import path
from reviews import views


urlpatterns = [
    path('', views.ReviewList.as_view()),
    path('<int:gig_id>', views.ReviewIndividual.as_view())
]
