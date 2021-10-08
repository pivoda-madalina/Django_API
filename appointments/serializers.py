from rest_framework import serializers
from .models import Client, Appointment


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'url', 'first_name', 'last_name', 'e_mail', 'phone')


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields = ('id', 'url', 'person', 'service', 'type', 'start_date', 'end_date')
