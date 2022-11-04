from django.contrib import admin
from django.urls import path, include
from .views import ClientCreateView, ClientDetailView, LoginAPIView

app_name = 'client'
urlpatterns = [
    path('register/', ClientCreateView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('user/<int:pk>/', ClientDetailView.as_view()),
]