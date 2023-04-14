from django.urls import path, include, re_path
from .views import (
    DoneeListCreate, DoneeDetail, 
    DonationAPIView, UserProfileViewSet,
    UserProfileMultiPartParserViewSet
    )
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'subscriber_profiles', UserProfileViewSet)
router.register(r'user_profiles_mpp', UserProfileMultiPartParserViewSet)

urlpatterns = [
    path('', views.api_root),
    path('donees/', DoneeListCreate.as_view(), name="donee_list"),
    path('donees/<int:pk>/', DoneeDetail.as_view(), name="donee_detail"),
    re_path(r'^', include(router.urls)),

    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    
    path('donation/', DonationAPIView.as_view(), name="donation" ),

    path('api-auth/', include('rest_framework.urls')),
]