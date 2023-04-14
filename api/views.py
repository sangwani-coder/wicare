# views.py
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .models import Donee, Donation, UserProfile
from .serializers import (
    DoneeSerializer, DonationSerializer,
    UserSerializer, UserProfileSerializer
    )

from .permissions import IsSubscriberOrReadOnly

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

# For user profile viewset
from rest_framework.decorators import action, parser_classes
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import status
from rest_framework.viewsets import GenericViewSet


@api_view(['GET'])
def api_root(request, format=None):
    """
    Base URL APIView. returns url endpoints for the WiCare API.
    """
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'donees': reverse('donee_list', request=request, format=format),
        'donations': reverse('donation', request=request, format=format),
        'register-user': reverse('register', request=request, format=format),
        'login-user': reverse('login', request=request, format=format),
        'logout-user': reverse('logout', request=request, format=format),
        'logoutall-user': reverse('logoutall', request=request, format=format),
    })


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
       IsSubscriberOrReadOnly,
    ]
    serializer_class = DoneeSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DoneeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Donee API view for Update requests.
    """
    permission_classes = [
        IsSubscriberOrReadOnly,
    ]
    queryset = Donee.objects.all()
    serializer_class = DoneeSerializer


class DonationAPIView(generics.ListCreateAPIView):
    """
    Donations API view for GET and POST requests.
    """
    # permission_classes = [
    #     permissions.IsAuthenticatedOrReadOnly,
    # ]
    queryset = Donation.objects.all().order_by('date_created')
    serializer_class = DonationSerializer


class UserProfileViewSet(
    RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    """
    We have a GenericViewSet combined with RetrieveModelMixin and 
    UpdateModelMixin to provide retrieve and update funcionality for our
    UserProfile model.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [
        IsSubscriberOrReadOnly,
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @action(
        detail=True,
        methods=['POST'],
        permission_classes=[
            IsSubscriberOrReadOnly,
            ])
    @parser_classes((FormParser, MultiPartParser,))
    def image(self, request, *args, **kwargs):
        """
        The image method is exposed as a view using @action decorator.
        The method is also decorated using @parser_classes where we declare
        that the requests should be parsed using FormParser or MultiPartParser,
        and this is what is going to allow us to handle the uploaded files.
        """
        
        if 'upload' in request.data:
            # When the method is invoked, we check that the request data
            # contains an upload entry, and if it does we delete the image
            # associated with the user profile, replace it with the
            # UploadedFile contents and return a Response.
             
            user_profile = self.get_object()
            user_profile.image.delete()

            upload = request.data['upload']

            user_profile.image.save(upload.name, upload)

            return Response(
                status=status.HTTP_201_CREATED,
                headers={'Location': user_profile.image.url})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserProfileMultiPartParserViewSet(
    RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    """
    Updates the the image as well as the model in a single request.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsSubscriberOrReadOnly,)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @parser_classes((MultiPartParser,))
    def update(self, request, *args, **kwargs):
        if 'upload' in request.data:
            user_profile = self.get_object()

            user_profile.image.delete()

            upload = request.data['upload']

            user_profile.image.save(upload.name, upload)

        return super(
            UserProfileMultiPartParserViewSet, self).update(
                request, *args, **kwargs)