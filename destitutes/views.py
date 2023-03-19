from destitutes.models import Education, Health
from destitutes.serializers import (
    DestituteEducationSerializer,
    DestituteHealthSerializer
    )
from rest_framework import viewsets
from django.contrib.auth.models import User
  
class EducationViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`,
    `retrive`, `update` and `destroy` actions.
    """
    queryset = Education.objects.all()
    serializer_class = DestituteEducationSerializer

    def perform_create(self, serializer):
        serializer.save(volunteer=self.request.user)

class HealthViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`,
    `retrive`, `update` and `destroy` actions.
    """
    queryset = Health.objects.all()
    serializer_class = DestituteHealthSerializer

    def perform_create(self, serializer):
        serializer.save(hospital=self.request.user)