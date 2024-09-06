from rest_framework import serializers
from . import models


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Booking
        fields = ['name', 'no_of_guests', 'booking_date']


class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Menu
        fields = ['id', 'title', 'price', 'inventory']
        read_only = ['id']