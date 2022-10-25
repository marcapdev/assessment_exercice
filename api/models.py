from django.utils.translation import gettext_lazy as _
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    phone = PhoneNumberField(_("phone number"), blank=False, null=False)
    email = models.EmailField(_("email address"), blank=False, null=False, unique=True)
    hobbies = models.TextField(_("hobbies"), blank=True)
    validated_phone = models.BooleanField(_("validated phone"), blank=False, null=False, default=False)
    validated_email = models.BooleanField(_("validated email"), blank=False, null=False, default=False)

    username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "phone", "hobbies"]

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return f'first_name: {self.first_name}, last_name: {self.last_name}'
