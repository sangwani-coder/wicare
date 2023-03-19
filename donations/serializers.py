from rest_framework import serializers
from donations.models import Donations

class Donationserializer(serializers.HyperlinkedModelSerializer):
    """
    serializes and deserializes the donations instances 
    into a json representation.
    """
    url= serializers.HyperlinkedRelatedField(
        many=True, view_name='donations:detail', read_only=True)
    class Meta:
        model = Donations
        fields = ['created', 'sponsor', 'amount',
                  'donate_to','mobile','email','url'
                ]