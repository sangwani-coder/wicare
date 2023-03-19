from rest_framework import serializers
from destitutes.models import Education, Health

class DestituteEducationSerializer(serializers.HyperlinkedModelSerializer):
    """
    serializes and deserializes the destitutes instances 
    into a json representation.
    """
    url= serializers.HyperlinkedRelatedField(
        many=True, view_name='education:detail', read_only=True)
    
    class Meta:
        model = Education
        fields = ['created', 'volunteer', 'familyname',
                  'shortstory','problemdescription','image','monthlybudget',
                  'url'
                ]

class DestituteHealthSerializer(serializers.HyperlinkedModelSerializer):
    """
    serializes and deserializes the destitutes instances 
    into a json representation.
    """
    url= serializers.HyperlinkedRelatedField(
        many=True, view_name='health:detail', read_only=True)
    class Meta:
        model = Health
        fields = ['created','patientsnames','patientsage','patientsphoto',
                  'hospital','medicalcondition','requiredfunds',
                  'requiredtreatment','urgent','url'
                ]