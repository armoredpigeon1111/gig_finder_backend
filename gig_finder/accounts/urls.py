from django.urls import path
from accounts import views


urlpatterns = [
    path('<int:id>/users', views.UserIndividual.as_view()),
]