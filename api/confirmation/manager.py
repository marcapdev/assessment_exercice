from celery import group
from api.confirmation import celery_task
from django.conf import settings
import importlib
from abc import ABC, abstractmethod


class AbstractConfirmationManager(ABC):
    task_map = {}  # maps sending protocol (sms | mail) with celery task

    @abstractmethod
    def send_confirmation(self, sms=None, mail=None):
        """
        Sends confirmation sms and mails (To be implemented by child class)
        @param sms: List of phone contacts
        @param mail: List of mail contacts
        @return:
        """
        pass

    def run_tasks(self, sms=None, mail=None):
        """
        Runs task
        @param sms: List of phone contacts
        @param mail: List of mail contacts
        @return:
        """
        if sms is not None:
            self.task_map.get('sms')(sms)
        if mail is not None:
            self.task_map.get('mail')(mail)


class ConfirmationManager(AbstractConfirmationManager):
    task_map = {
        'sms': celery_task.send_sms,
        'mail': celery_task.send_mail,
    }

    def send_confirmation(self, sms=None, mail=None):
        super().run_tasks(sms=sms, mail=mail)


class MockupConfirmationManager(AbstractConfirmationManager):
    task_map = {
        'sms': celery_task.send_sms_mockup,
        'mail': celery_task.send_mail_mockup,
    }

    def send_confirmation(self, sms=False, mail=False):
        super().run_tasks(sms=sms, mail=mail)
        # In some cases task id might come at handy for tracking purposes


class ConfirmationBuilder:
    @staticmethod
    def get_confirmation_manager_instance() -> 'AbstractConfirmationManager':
        """
        Returns AbstractConfirmationManager implementation depending on environment (local / production)
        @rtype: AbstractConfirmationManager
        """
        manager_mod = importlib.import_module(settings.CONFIRMATION_MANAGER_MODULE)
        manager_class = getattr(manager_mod, settings.CONFIRMATION_MANAGER_CLASS)
        return manager_class()
