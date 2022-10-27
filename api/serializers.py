from rest_framework import serializers
from django.core import exceptions
import django.contrib.auth.password_validation as password_validator

from api.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'hobbies',
            'validated_phone',
            'validated_email',
            'password'
        ]
        read_only_fields = ('validated_phone', 'validated_email')

        extra_kwargs = {
            'password': {'write_only': True, "required": True, "allow_null": False}
        }

    def validate(self, data):
        user = User(**data)

        password = data.get('password')

        errors = dict()
        try:
            password_validator.validate_password(password=password, user=user)

        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

        return super(UserSerializer, self).validate(data)

    def create(self, validated_data):
        model_class = self.Meta.model
        user = model_class(**validated_data)
        if 'password' in validated_data:
            user.set_password(validated_data['password'])
        user.save()

        return user
