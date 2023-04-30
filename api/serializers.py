# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Donee, Donation, UserProfile

from . import choices


class UserSerializer(serializers.ModelSerializer):
    donees = serializers.PrimaryKeyRelatedField(many=True, queryset=Donee.objects.all())
    profile = serializers.PrimaryKeyRelatedField(many=True, queryset=UserProfile.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'donees', 'profile']


class ChoiceField(serializers.ChoiceField):

    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]

    def to_internal_value(self, data):
        # To support inserts with the value
        if data == '' and self.allow_blank:
            return ''

        for key, val in self._choices.items():
            if val == data:
                return key
        self.fail('invalid_choice', input=data)

class DoneeSerializer(serializers.ModelSerializer):
    location = ChoiceField(
        choices=choices.ZAMBIAN_PROVINCE_CHOICES, allow_blank=True)
    cause =ChoiceField(choices=choices.CAUSES_CHOICES)


    class Meta:
        model = Donee
        fields = (
            'id', 'full_name', 'location','cause',
            'bio', 'need', 'image' ,'amount_needed')

        read_only_fields = ('image',)


class DonationSerializer(serializers.ModelSerializer):
    location = ChoiceField(
        choices=choices.ZAMBIAN_PROVINCE_CHOICES, allow_blank=True)
    cause =ChoiceField(choices=choices.CAUSES_CHOICES)

    class Meta:
        model = Donation
        fields = (
            'id', 'cause', 'donor_full_names', 'location',
            'amount_donated', 'comment',  'account_number')
        
        read_only_fields = ('location', 'cause')



class UserProfileSerializer(serializers.ModelSerializer):
    location = ChoiceField(
        choices=choices.ZAMBIAN_PROVINCE_CHOICES, allow_blank=True)
    gender = ChoiceField(choices=choices.GENDER_CHOICES)
    class Meta:
        model = UserProfile
        fields = (
            'gender',
            'user_profile',
            'is_nurse',
            'is_teacher',
            'is_donor',
            'phone_number',
            'account_number',
            'location',
            'bio',
            'image',
        )
        # Given that it is not possible to
        # handle uploads using the default JSON parser,
        # we marked the image field as read-only.
        read_only_fields = ('image',)