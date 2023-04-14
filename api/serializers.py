# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Donee, Donation, UserProfile

from .choices import ModelChoices


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
        choices=ModelChoices.ZAMBIAN_PROVINCE_CHOICES, allow_blank=True)

    class Meta:
        model = Donee
        fields = ('id', 'full_name', 'location', 'bio', 'need', 'image')

        read_only_fields = ('image',)


class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ('__all__')


class UserProfileSerializer(serializers.ModelSerializer):
    gender = serializers.ChoiceField(
        choices=ModelChoices.GENDER_CHOICES, allow_blank=True)
    location = serializers.ChoiceField(
        choices=ModelChoices.ZAMBIAN_PROVINCE_CHOICES, allow_blank=True)
    class Meta:
        model = UserProfile
        fields = (
            'user',
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
        readonly_fields = ('image')