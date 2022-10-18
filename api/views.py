from rest_framework import generics

from api.models import User
from api.serializers import UserSerializer


# Create your views here.
class UserCreateAPIView(
    generics.CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        super().perform_create(serializer)
        # if saved, send confirmation SMS and Mail


user_create_view = UserCreateAPIView.as_view()


class UserDetailAPIView(
    generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


user_detail_view = UserDetailAPIView.as_view()
