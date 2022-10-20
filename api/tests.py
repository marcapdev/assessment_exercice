from django.db import IntegrityError, DataError
from django.test import TestCase

from api.models import User


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(first_name="Marc", last_name="Amposta Pérez", email="marc.amposta.perez93@gmail.com",
                            phone="+34616650957", hobbies="test")

    def test_existing_mail(self):
        """
        Test adding entry with duplicated mail
        @return:
        """
        with self.assertRaises(IntegrityError):
            User.objects.create(first_name="Marc", last_name="Amposta Pérez", email="marc.amposta.perez93@gmail.com",
                                phone="+34616650957", hobbies="test")

    def test_phone_format(self):
        """
        Test adding entry with wrong phone format
        @return:
        """
        with self.assertRaises(IntegrityError):
            User.objects.create(first_name="Marc", last_name="Amposta Pérez", email="marc.amposta.perez93@gmail.com",
                                phone="+34616650957123", hobbies="test")

    def test_length_overflow(self):
        """
        Test adding entry that exceeds length Limit
        @return:
        """
        long_text = "a" * 100000000
        with self.assertRaises(DataError):
            User.objects.create(first_name="Marc", last_name=long_text,
                                email="marc.amposta.perez93@gmail.com",
                                phone="+34616650957123", hobbies="test")
