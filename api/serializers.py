from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.utils.translation import gettext_lazy as _

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
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        model_class = self.Meta.model
        user = model_class(**validated_data)
        if 'password' in validated_data:
            user.set_password(validated_data['password'])
            user.save()

        return user


class NoPasswordAuthTokenSerializer(AuthTokenSerializer):
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True,
        required=False,
        allow_blank=True
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user = authenticate(request=self.context.get('request'),
                            username=username, password=password)

        if not user:
            msg = _('Unable to log in with provided credentials.')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
