from django.urls import path
from rsvps import views


urlpatterns = [
    path('', views.RSVPList.as_view()),
    path('<int:fan_id>', views.RSVPFan.as_view())
]