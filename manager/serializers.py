from rest_framework import serializers
from . import models


class PasswordSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'email', 'name', 'website', 'password')
        model = models.PasswordRecord


class PasswordListSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'email', 'name', 'website')
        model = models.PasswordRecord
