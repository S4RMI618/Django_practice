from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index/', views.index),
    path('about/', views.about),
    path('hello/<str:username>', views.hello),
    path('projects/', views.projects),
    path('tasks/', views.tasks),
    path('create_tasks/', views.createTask)
]