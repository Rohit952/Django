from django.urls import path
# from .views import template_view
from TestApp2 import views  # the above 2 methods are working

urlpatterns = [
    path('app/', views.template_view),
    path('wish/', views.wish),
]