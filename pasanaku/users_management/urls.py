from django.urls import path
from . import views

urlpatterns = [
    path('user/<str:id>', views.userData, name='id'),
    path('users/', views.users, name='users')
]