from django.urls import path, include
# from .views import Hello_World, date_time_view
from TestApp4 import views

urlpatterns = [
    path('', views.employee_info_view)
]
