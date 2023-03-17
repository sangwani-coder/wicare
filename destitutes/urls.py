from django.urls import path, include
from rest_framework.routers import DefaultRouter
from destitutes import views
from donations.views import DonationsViewSet
from subscribers.views import SubscriberViewSet, UserViewSet

router = DefaultRouter()

router.register(r'education', views.DestitutesEducationViewSet,basename='education')
router.register(r'health', views.DestitutesHealthViewSet,basename='health')
router.register(r'donations', DonationsViewSet,basename='donations')
router.register(r'subscribers', SubscriberViewSet,basename="subscribers")
router.register(r'users', UserViewSet,basename='user')

urlpatterns = [
    path('', include(router.urls)),
]