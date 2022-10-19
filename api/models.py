from django.utils.translation import gettext_lazy as _
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class User(models.Model):
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), blank=True, null=False, unique=True)
    phone = PhoneNumberField(_("phone number"), blank=False, null=False)
    hobbies = models.TextField(_("hobbies"), blank=True)
    validated_phone = models.BooleanField(_("validated phone"), blank=False, null=False, default=False)
    validated_email = models.BooleanField(_("validated email"), blank=False, null=False, default=False)
