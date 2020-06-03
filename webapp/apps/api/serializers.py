from rest_framework import serializers
from api.models import *

# class MySerializer(serializers.ModelSerializer):

#     class Meta:
#         model = MyModel
#         exclude = ('is_deleted', 'modified_at', 'created_at')


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        exclude = ('is_deleted', 'modified_at', 'created_at')


class FacilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Facility
        exclude = ('is_deleted', 'modified_at', 'created_at')


class ParkingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parking
        exclude = ('is_deleted', 'modified_at', 'created_at')
