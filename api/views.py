from django.db import transaction
from kombu.exceptions import OperationalError
from rest_framework import generics

from api.confirmation.manager import ConfirmationBuilder
from api.models import User
from api.serializers import UserSerializer
from backend_assessment_exercice.exceptions import ServiceUnavailableError


class UserCreateAPIView(
    generics.CreateAPIView):
    serializer_class = UserSerializer

    @transaction.atomic
    def perform_create(self, serializer):
        super().perform_create(serializer)
        # if saved, send confirmation SMS and Mail
        try:
            manager_instance = ConfirmationBuilder.get_confirmation_manager_instance()
            manager_instance.send_confirmation_sms()
            manager_instance.send_confirmation_mail()
        except OperationalError:
            raise ServiceUnavailableError("Couldn't send verification sms and mail")


user_create_view = UserCreateAPIView.as_view()


class UserDetailAPIView(
    generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


user_detail_view = UserDetailAPIView.as_view()
