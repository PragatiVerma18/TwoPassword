from django.shortcuts import render
from rest_framework import generics
import django_filters.rest_framework
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import PasswordRecord
from .serializers import PasswordSerializer, PasswordListSerializer
from rest_framework.response import Response
from django.core.exceptions import PermissionDenied
from rest_framework import status

from manager import serializers


class PasswordList(generics.ListAPIView):
    serializer_class = PasswordListSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

    def get_queryset(self):
        user = self.request.user
        return PasswordRecord.objects.filter(email=user.email)


class PasswordCreate(generics.CreateAPIView):
    serializer_class = PasswordSerializer

    def perform_create(self, serializer):
        if serializer.validated_data['email'] != self.request.user.email:
            raise PermissionDenied()

        serializer.save()


class PasswordDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PasswordSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

    def get_queryset(self):
        user = self.request.user
        return PasswordRecord.objects.filter(email=user.email)
