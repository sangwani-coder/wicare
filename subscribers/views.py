from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from subscribers.models import Subscribers
from subscribers.serializers import SubscriberSerializer, UserSerializer
from rest_framework import generics
from subscribers.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from rest_framework import permissions

from rest_framework import renderers

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'subscribers': reverse('subscribers-list', request=request, format=format)
    })

class SubscribersHighlight(generics.GenericAPIView):
    queryset = Subscribers.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        subscriber = self.get_object()
        return Response(subscriber.highlighted)
    
class SubscriberList(generics.ListCreateAPIView):
    """
    List all subscribers, or create a new subscriber.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Subscribers.objects.all()
    serializer_class = SubscriberSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SubscriberDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, delete a subscriber.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    queryset = Subscribers.objects.all()
    serializer_class = SubscriberSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer