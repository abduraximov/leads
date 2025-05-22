from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate


class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=255, required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        phone = attrs.get("phone")
        password = attrs.get("password")

        user = authenticate(username=phone, password=password)

        if not user:
            raise serializers.ValidationError(_("Invalid credentials"), code="invalid_credentials")

        return user