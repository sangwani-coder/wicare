from destitutes.models import DestitutesEducation, DestitutesHealth
from destitutes.serializers import (
    DestituteEducationSerializer,
    DestituteHealthSerializer
    )
from rest_framework import viewsets
from django.contrib.auth.models import User
  
class DestitutesEducationViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`,
    `retrive`, `update` and `destroy` actions.
    """
    queryset = DestitutesEducation.objects.all()
    serializer_class = DestituteEducationSerializer

    def perform_create(self, serializer):
        serializer.save(caregiver=self.request.user)

class DestitutesHealthViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`,
    `retrive`, `update` and `destroy` actions.
    """
    queryset = DestitutesHealth.objects.all()
    serializer_class = DestituteHealthSerializer

    def perform_create(self, serializer):
        serializer.save(hospital=self.request.user)