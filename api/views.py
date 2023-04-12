# views.py
from rest_framework import generics, permissions
from .models import Donee
from .serializers import DoneeSerializer

class DoneeList(generics.ListAPIView):
    queryset = Donee.objects.all().order_by('id')
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = DoneeSerializer


class DoneeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Donee.objects.all()
    serializer_class = DoneeSerializer
