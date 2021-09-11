from django.urls import path
from . import views

urlpatterns = [
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('update/<int:pk>/', views.update, name='update'),
    path('', views.index, name='index'),
]