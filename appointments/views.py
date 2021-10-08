from django.shortcuts import render
from rest_framework import viewsets
from .models import Appointment, Client
from .serializers import AppointmentSerializer, ClientSerializer


class ClientView(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class AppointmentView(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
