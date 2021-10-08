from django.urls import path
from fans import views


urlpatterns = [
    path('', views.FanList.as_view()),
    path('<int:user_id>/', views.FanIndividual.as_view()),
    # path('<int:user_id>/fan', views.FanIndividual.as_view())
]
