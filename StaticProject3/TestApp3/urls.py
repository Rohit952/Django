from django.urls import path
from TestApp3 import views

urlpatterns = [
    path('wish/', views.wish),
]