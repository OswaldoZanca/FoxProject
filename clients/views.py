"""
API's to client app
"""
from rest_framework import generics
from clients.models import Client
from clients.serializers import (
    ClientReadSerializer,
    ClientWriteSerializer
)


class ClientListCreateView(generics.ListCreateAPIView):
    """
    Api to list and create a new client
    """
    queryset = Client.objects.all()
    
    def get_serializer_class(self):
        """
        Get serializer
        """
        if self.request.method == 'POST':
            return ClientWriteSerializer
        return ClientReadSerializer


class ClientRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Api to retrive, update and delete a client
    """
    queryset = Client.objects.all()

    def get_serializer_class(self):
        """
        Get serializer
        """
        if self.request.method in ['PUT', 'PATCH']:
            return ClientWriteSerializer
        return ClientReadSerializer