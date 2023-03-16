from donations.models import Donations
from donations.serializers import Donationserializer
from rest_framework import viewsets
  
    
class DonationsViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`,
    `retrive`, `update` and `destroy` actions.
    """
    queryset = Donations.objects.all()
    serializer_class = Donationserializer