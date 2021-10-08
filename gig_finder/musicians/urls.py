from django.urls import path
from musicians import views


urlpatterns = [
    path('', views.MusicianList.as_view()),
    path('<int:user_id>', views.MusicianIndividual.as_view())
]
