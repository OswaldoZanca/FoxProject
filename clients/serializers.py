"""
Serializer of clients app
"""
from rest_framework import serializers
from .models import Client


class ClientReadSerializer(serializers.ModelSerializer):
    """
    Serializer to read a client
    """
    class Meta:
        """
        Meta
        """
        model = Client
        fields = [
            'id',
            'name',
            'email',
            'address',
            'phone_number',
            'created_at',
            'update_at'
        ]
        read_only_fields = ['id', 'created_at', 'update_at']
        

class ClientWriteSerializer(serializers.ModelSerializer):
    """
    Serializer to write a client
    """
    class Meta:
        """
        Meta
        """
        model = Client
        fields = [
            'name',
            'email',
            'address',
            'phone_number',
        ]