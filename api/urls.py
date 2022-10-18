from django.urls import path

from . import views
from django.conf import settings

# /api/{{VERSION_API}}/
urlpatterns = [
    path(f'api/{settings.VERSION_API}', views.user_create_view, name='user-create'),
]
