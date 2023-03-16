from rest_framework import serializers
from destitutes.models import Destitutes

class Destituteserializer(serializers.HyperlinkedModelSerializer):
    """
    serializes and deserializes the destitutes instances 
    into a json representation.
    """
    caregiver = serializers.ReadOnlyField(source='caregiver.username')
    class Meta:
        model = Destitutes
        look_up_field = 'caregiver'
        fields = ['created', 'caregiver', 'familyname',
                  'shortstory','problemdescription','image','monthlybudget',
                  'url'
                ]