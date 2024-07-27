from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('result/<path:output_url>/', views.result, name='result'),
    path('download/<str:format>/', views.download_image, name='download'),
]