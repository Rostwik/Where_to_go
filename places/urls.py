from places import views
from django.urls import path, include

urlpatterns = [
                  path('', views.index),
                  path('places/<int:id>/', views.places, name='api_place'),
]