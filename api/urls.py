from django.urls import path, include
from .views import (
    DoneeListCreate, DoneeDetail, 
    DonationAPIView, UserProfileAPIView
    )
from . import views

urlpatterns = [
    path('donees/', DoneeListCreate.as_view(), name="donee_list"),
    path('donees/<int:pk>/', DoneeDetail.as_view(), name="donee_detail"),
    path('donees/profile/', UserProfileAPIView.as_view(), name='profile'),

    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    
    path('donation/', DonationAPIView.as_view(), name="donation" ),
    # path('donors/profile', DonationAPIView.as_view(), name="donation" ),

    path('api-auth/', include('rest_framework.urls')),
]