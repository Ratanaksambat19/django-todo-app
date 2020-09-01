from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('update_todo/<str:pk>/', views.updateTask, name = 'update_todo'),
    path('delete/<str:pk>/', views.deleteTask, name = 'delete'),

]
