from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.user_create_view, name='user-create'),
    path('profile/<int:pk>/', views.user_detail_view, name='user-detail'),
]
