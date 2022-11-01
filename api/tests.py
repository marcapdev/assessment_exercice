from django.db import IntegrityError, DataError
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIRequestFactory
from api.models import User
from api.views import UserCreateAPIView, UserDetailAPIView


class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(first_name="Marc", last_name="Amposta Pérez",
                                        email="marc.amposta.perez93@gmail.com",
                                        phone="+34616650957", hobbies="test",
                                        password="pbkdf2_sha256$320000$Us9LYQSXHZ8Q4DSGf0YBQZ$UhpJyYw7mjJLrFSE6PScrDUrQ3o2ECwrXl0uSUXsXpo=")
        self.token = Token.objects.create(key="65cff87d64c545eb1c48a5eba4bb0bbf92a79356", user=self.user)

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


class UserEndpointsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(first_name="Marc", last_name="Amposta Pérez",
                                        email="marc.amposta.perez93@gmail.com",
                                        phone="+34616650957", hobbies="test",
                                        password="pbkdf2_sha256$320000$Us9LYQSXHZ8Q4DSGf0YBQZ$UhpJyYw7mjJLrFSE6PScrDUrQ3o2ECwrXl0uSUXsXpo=")
        self.token = Token.objects.create(key="65cff87d64c545eb1c48a5eba4bb0bbf92a79356", user=self.user)

        self.factory = APIRequestFactory()

    def test_register_user(self):
        post_data = {
            "first_name": "Marc",
            "last_name": "Amposta Pérez",
            "email": "marc.amposta.perez96@gmail.com",
            "phone": "+34964052238",
            "hobbies": "test de prueba para comprobar ....",
            "password": "12341234@"
        }
        request = self.factory.post(reverse("user-create"), post_data)
        view = UserCreateAPIView.as_view()

        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_user_dup_email(self):
        post_data = {
            "first_name": "Marc",
            "last_name": "Amposta Pérez",
            "email": "marc.amposta.perez93@gmail.com",
            "phone": "+34964052238",
            "hobbies": "test de prueba para comprobar ....",
            "password": "12341234@"
        }
        request = self.factory.post(reverse("user-create"), post_data)
        view = UserCreateAPIView.as_view()

        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_user_no_email(self):
        post_data = {
            "first_name": "Marc",
            "last_name": "Amposta Pérez",
            "phone": "+34964052238",
            "hobbies": "test de prueba para comprobar ....",
            "password": "12341234@"
        }
        request = self.factory.post(reverse("user-create"), post_data)
        view = UserCreateAPIView.as_view()

        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_user_inject_read_only_info_and_password_read_only(self):
        post_data = {
            "first_name": "Marc",
            "email": "marc.amposta.perez98@gmail.com",
            "last_name": "Amposta Pérez",
            "phone": "+34964052238",
            "hobbies": "test de prueba para comprobar ....",
            "password": "12341234@",
            "validated_phone": True
        }
        expected = {
            "first_name": "Marc",
            "last_name": "Amposta Pérez",
            "email": "marc.amposta.perez98@gmail.com",
            "phone": "+34964052238",
            "hobbies": "test de prueba para comprobar ....",
            "validated_phone": False,
            "validated_email": False
        }
        request = self.factory.post(reverse("user-create"), post_data)
        view = UserCreateAPIView.as_view()

        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(expected, response.data)

    def test_user_profile(self):
        expected = {
            "first_name": "Marc",
            "last_name": "Amposta Pérez",
            "email": "marc.amposta.perez93@gmail.com",
            "phone": "+34616650957",
            "hobbies": "test",
            "validated_phone": False,
            "validated_email": False
        }

        request = self.factory.get(reverse("user-detail"), HTTP_AUTHORIZATION=f'Token {self.token.key}')
        view = UserDetailAPIView.as_view()

        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(expected, response.data)
