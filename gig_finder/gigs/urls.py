from django.urls import path
from gigs import views


urlpatterns = [
    path('', views.GigList.as_view()),
    path('<int:pk>/', views.GigIndividual.as_view()),
    path('<int:pk>/delete', views.GigDelete.as_view()),
    path('<int:pk>/like', views.GigLike.as_view()),
    path('<int:pk>/update', views.GigUpdate.as_view()),
    

]
