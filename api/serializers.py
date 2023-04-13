# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Donee, Donation, UserProfile

class UserSerializer(serializers.ModelSerializer):
    donees = serializers.PrimaryKeyRelatedField(many=True, queryset=Donee.objects.all())
    profile = serializers.PrimaryKeyRelatedField(many=True, queryset=UserProfile.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'donees', 'profile']

class DoneeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donee
        fields = ('id', 'full_name', 'location', 'bio', 'need')


class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ('__all__')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            'user',
            'is_nurse',
            'is_teacher',
            'identification_type',
            'identification_number',
            'mobile_number',
            'account_number',
            'location',
            'bio'
        )