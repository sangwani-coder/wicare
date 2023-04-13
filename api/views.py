# views.py
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .models import Donee, Donation, UserProfile
from .serializers import (
    DoneeSerializer, DonationSerializer,
    UserSerializer, UserProfileSerializer
    )


class UserList(generics.ListAPIView):
    """
    User Get API View
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """
    User Update API View
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DoneeListCreate(generics.ListCreateAPIView):
    """
    Donee API view for GET and POST requests.
    """
    queryset = Donee.objects.all().order_by('id')
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]
    serializer_class = DoneeSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DoneeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Donee API view for Update requests.
    """
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Donee.objects.all()
    serializer_class = DoneeSerializer


class DonationAPIView(generics.ListCreateAPIView):
    """
    Donations API view for GET and POST requests.
    """
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]
    queryset = Donation.objects.all().order_by('date_created')
    serializer_class = DonationSerializer


class UserProfileAPIView(generics.ListCreateAPIView):
    """
    UserProfile View
    """
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]
    queryset = UserProfile.objects.all().order_by('id')
    serializer_class = UserProfileSerializer