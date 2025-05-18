"""
Model of clients
"""
from django.db import models

class Client(models.Model):
    """
    Model of client
    """
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    password = models.CharField(max_length=255, null=False, blank=False)
    address = models.CharField(max_length=255, null=False, blank=False)
    phone_number = models.CharField(max_length=9, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_ay = models.DateTimeField(auto_now=True)
    

