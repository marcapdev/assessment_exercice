from django.urls import path

from . import views 
from backend.settings import VERSION_API
# /api/{{VERSION_API}}/
urlpatterns = [

    path(f'api/{{VERSION_API}}', views.user_create_view, name='user-create'),
]