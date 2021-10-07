from django.urls import path
from fans import views


urlpatterns = [
    path('', views.FanList.as_view()),
    path('<int:id>/', views.FanList.as_view())
]
