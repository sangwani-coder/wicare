from rest_framework import serializers
from subscribers.models import Subscribers
from django.contrib.auth.models import User

class SubscriberSerializer(serializers.HyperlinkedModelSerializer):
    """
    serializes and deserializes the subscribers instances 
    into json representation.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Subscribers
        look_up_field = 'owner'
        fields = ['created', 'id', 'owner',
                  'firstname','lastname', 
                  'location','mobile','email', 'url'
                  ]

class UserSerializer(serializers.HyperlinkedModelSerializer):
    subscribers = serializers.HyperlinkedRelatedField(
        many=True, view_name='subscribers-detail', read_only=True)
    
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'subscribers']