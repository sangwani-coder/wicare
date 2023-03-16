from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from subscribers.models import Subscribers
from subscribers.serializers import SubscriberSerializer, UserSerializer
from rest_framework import generics
from subscribers.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from rest_framework import permissions

from rest_framework import viewsets

class SubscriberViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`,
    `retrive`, `update` and `destroy` actions.
    """
    queryset = Subscribers.objects.all()
    serializer_class = SubscriberSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrive` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer