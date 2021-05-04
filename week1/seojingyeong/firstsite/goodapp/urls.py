from django.urls import path
from . import views

urlpatterns = [
    path('namecard/', views.index, name='index'),
]