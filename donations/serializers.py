from rest_framework import serializers
from donations.models import Donations

class Donationserializer(serializers.HyperlinkedModelSerializer):
    """
    serializes and deserializes the donations instances 
    into a json representation.
    """
    class Meta:
        model = Donations
        fields = ['created', 'sponsor', 'amount',
                  'donate_to','mobile','email','url'
                ]