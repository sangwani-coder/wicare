# api/urls.py
from django.urls import path, include
from rest_framework import routers
from .views import (
    api_root, UserList, UserDetail,
    DoneeListCreate,
    DoneeDetail, DonationAPIView,
    UserProfileViewSet,
    UserProfileMultiPartParserViewSet)


router = routers.DefaultRouter()
router.register(r'userprofile',
    UserProfileViewSet, basename='profile-list')
# router.register(r'user-profile-multipart',
    # UserProfileMultiPartParserViewSet, basename='profile-multipart')

urlpatterns = [
    path('', api_root),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('donees/', DoneeListCreate.as_view(), name='donee_list'),
    path('donees/<int:pk>/', DoneeDetail.as_view(), name='donee_detail'),
    path('donations/', DonationAPIView.as_view(), name='donation'),
    path('auth/', include('accounts.urls')),
]
urlpatterns += router.urls