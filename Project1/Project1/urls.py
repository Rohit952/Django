"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from TestApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
<<<<<<< HEAD
    path('pycharm/', views.home, name='home'),
=======
    path('pycharm', views.home, name='home'),
>>>>>>> e7a70893256a6d150762948c91c9249eb8ac51ca
=======
    path('pycharm', views.home, name='home'),
>>>>>>> e7a70893256a6d150762948c91c9249eb8ac51ca
    path('app/', include('TestApp.urls')),
]