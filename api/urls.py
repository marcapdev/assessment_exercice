from django.urls import path

from . import views
from .views import obtain_auth_token

urlpatterns = [
    path('signup/', views.user_create_view, name='user-create'),
    path('profile/', views.user_detail_view, name='user-detail'),
    path('api-token-auth/', obtain_auth_token, name='get-token')

]
