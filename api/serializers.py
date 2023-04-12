# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Donee

class DoneeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donee
        fields = ('id', 'full_name', 'location', 'bio', 'need')