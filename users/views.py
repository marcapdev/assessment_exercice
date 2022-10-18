from rest_framework import generics

from users.serializers import UserSerializer


# Create your views here.
class UserCreateAPIView(
    generics.CreateAPIView):
    serializer_class = UserSerializer


user_create_view = UserCreateAPIView.as_view()
