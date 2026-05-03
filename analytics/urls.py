from django.urls import path
from . import views

urlpatterns = [
    path('teacher/', views.teacher_analytics, name='teacher_analytics'),
]
