from celery import group
from api.message import celery_task
from django.conf import settings
import importlib
from abc import ABC, abstractmethod


class AbstractMessageManager(ABC):
    task_map = {}  # maps sending protocol (sms | mail) with celery task

    @abstractmethod
    def send_message(self, sms=None, mail=None):
        """
        Sends msn sms and mails (To be implemented by child class)
        @param sms: List of phone contacts
        @param mail: List of mail contacts
        @return:
        """
        pass

    def get_tasks(self, sms=None, mail=None):
        """
        Prepares subtask for celery to run
        @param sms: List of phone contacts
        @param mail: List of mail contacts
        @return:
        """
        if sms is not None:
            yield self.task_map.get('sms').subtask(kwargs={"contacts": sms})
        if mail is not None:
            yield self.task_map.get('mail').subtask(kwargs={"contacts": mail})


class ConfirmationManager(AbstractMessageManager):
    task_map = {
        'sms': celery_task.send_sms_task,
        'mail': celery_task.send_mail_task,
    }

    def send_message(self, sms=None, mail=None):
        id = group(super().get_tasks(sms=sms, mail=mail)).delay()


class ConfirmationBuilder:
    @staticmethod
    def get_confirmation_manager_instance() -> 'AbstractMessageManager':
        """
        Returns AbstractConfirmationManager implementation depending on environment (local / production)
        @rtype: AbstractConfirmationManager
        """
        manager_mod = importlib.import_module(settings.MESSAGE_MANAGER_MODULE)
        manager_class = getattr(manager_mod, settings.CONFIRMATION_MANAGER_CLASS)
        return manager_class()
