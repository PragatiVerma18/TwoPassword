from django.shortcuts import render
from rest_framework import generics
import django_filters.rest_framework
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import PasswordRecord
from .serializers import PasswordSerializer, PasswordListSerializer
from rest_framework.response import Response


class PasswordList(generics.ListAPIView):
    queryset = PasswordRecord.objects.all()
    serializer_class = PasswordListSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]


class PasswordCreate(generics.CreateAPIView):
    queryset = PasswordRecord.objects.all()
    serializer_class = PasswordSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]


class PasswordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PasswordRecord.objects.all()
    serializer_class = PasswordSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]


class PasswordByUser(generics.ListAPIView):
    model = PasswordRecord
    serializer_class = PasswordListSerializer
    lookup_field = 'email'

    def get_queryset(self):
        email = self.kwargs['email']
        return PasswordRecord.objects.filter(email=email)
