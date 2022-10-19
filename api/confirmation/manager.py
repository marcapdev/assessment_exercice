import api.confirmation.celery_task as task
from django.conf import settings
import importlib
from abc import ABC, abstractmethod


class AbstractConfirmationManager(ABC):
    @abstractmethod
    def send_confirmation_sms(self):
        pass

    @abstractmethod
    def send_confirmation_mail(self):
        pass


class ConfirmationManager(AbstractConfirmationManager):
    def send_confirmation_sms(self):
        task_id = task.send_sms()
        # In some cases task id might come at handy for tracking purposes

    def send_confirmation_mail(self):
        task_id = task.send_mail()
        # In some cases task id might come at handy for tracking purposes


class MockupConfirmationManager(AbstractConfirmationManager):
    def send_confirmation_sms(self):
        task_id = task.send_sms_mockup.delay()
        # In some cases task id might come at handy for tracking purposes

    def send_confirmation_mail(self):
        task_id = task.send_mail_mockup.delay()
        # In some cases task id might come at handy for tracking purposes


class ConfirmationBuilder:
    @staticmethod
    def get_confirmation_manager_instance() -> 'AbstractConfirmationManager':
        """
        returns AbstractConfirmationManager implementation depending on environment(local / production)
        @rtype: AbstractConfirmationManager
        """
        manager_mod = importlib.import_module(settings.CONFIRMATION_MANAGER_MODULE)
        manager_class = getattr(manager_mod, settings.CONFIRMATION_MANAGER_CLASS)
        return manager_class()
