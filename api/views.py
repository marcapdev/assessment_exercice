from django.db import transaction
from kombu.exceptions import OperationalError
from rest_framework import generics
from django.utils.translation import gettext_lazy as _

from api.confirmation.manager import ConfirmationBuilder
from api.models import User
from api.serializers import UserSerializer
from backend_assessment_exercice.exceptions import ServiceUnavailableError


class UserCreateAPIView(
    generics.CreateAPIView):
    serializer_class = UserSerializer

    @transaction.atomic
    def perform_create(self, serializer):
        """
        Creates user in DB and sends verification mail and SMS
        Set transaction atomic to prevent user from being created if verification mail and sms task has not been added
        into celery task queue.
        @param serializer:
        @return:
        """
        user = serializer.save()
        # if saved, send confirmation SMS and Mail
        try:
            manager_instance = ConfirmationBuilder.get_confirmation_manager_instance()
            manager_instance.send_confirmation(sms=[user.phone.as_e164], mail=[user.email])
        except OperationalError:
            raise ServiceUnavailableError(_("Couldn't send verification SMS and mail"))


user_create_view = UserCreateAPIView.as_view()


class UserDetailAPIView(
    generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


user_detail_view = UserDetailAPIView.as_view()
