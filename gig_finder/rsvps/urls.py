from django.urls import path
from rsvps import views


urlpatterns = [
    path('', views.RSVPList.as_view())
]