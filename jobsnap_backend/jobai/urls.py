from django.urls import path
from . import views

urlpatterns = [
    path('generate-reply/', views.generate_reply, name='generate_reply'),
    path('generate-resume/', views.generate_resume, name='generate_resume'),
]







