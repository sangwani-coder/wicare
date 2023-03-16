from django.urls import path, include
from rest_framework.routers import DefaultRouter
from subscribers import views

router = DefaultRouter()

router.register(r'subscribers', views.SubscriberViewSet,basename="subscribers")
router.register(r'users', views.UserViewSet,basename='user')

urlpatterns = [
    path('', include(router.urls)),
]