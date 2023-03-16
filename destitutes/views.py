from destitutes.models import Destitutes
from destitutes.serializers import Destituteserializer
from rest_framework import viewsets
  
class DestitutesViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`,
    `retrive`, `update` and `destroy` actions.
    """
    queryset = Destitutes.objects.all()
    serializer_class = Destituteserializer

    def perform_create(self, serializer):
        serializer.save(caregiver=self.request.user)
