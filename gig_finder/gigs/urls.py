from django.urls import path
from gigs import views


urlpatterns = [
    path('', views.GigList.as_view()),
    path('<int:pk>/', views.GigIndividual.as_view()),

]
