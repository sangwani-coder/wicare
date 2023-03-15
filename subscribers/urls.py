from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from subscribers import views

urlpatterns = format_suffix_patterns([
    path('',views.api_root),
    path('subscribers/',
         views.SubscriberList.as_view(),
         name='subscribers-list'),
    path('subscribers/<int:pk>',
         views.SubscriberDetail.as_view(),
         name='subscribers-detail'),
    path('subscribers/<int:pk>/highlight',
         views.SubscribersHighlight.as_view(),
         name='SubscribersHighlight'),
    path('users/',
         views.UserList.as_view(),
         name='user-list'),
    path('users/<int:pk>',
         views.UserDetail.as_view(),
         name='user-detail'),
])