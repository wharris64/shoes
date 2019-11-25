"""ghostpost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from ghostpost import views, models 
from django.contrib import admin
from django.urls import path
admin.site.register(models.RoastBoast)
urlpatterns = [
    path('admin/', admin.site.urls),
    path("roastboastadd/", views.roastboastaddview),
    path('', views.index),
    path('boasts/', views.boasts),
    path('roasts/', views.roasts),
    path('popular/', views.popular),
    path('upvote/<int:id>/', views.upvote),
    path('downvote/<int:id>/', views.downvote)
    
]
