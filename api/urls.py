from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken

from . import views

urlpatterns = [
    path('signup/', views.user_create_view, name='user-create'),
    path('profile/', views.user_detail_view, name='user-detail'),
    path('api-token-auth/', ObtainAuthToken.as_view(), name='get-token')
]
