from django.urls import path, include
# from .views import Hello_World, date_time_view
from TestApp import views

urlpatterns = [
    path('hello/', views.Hello_World),
    path('date/', views.date_time_view)
]
