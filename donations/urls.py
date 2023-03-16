from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from donations import views

router = DefaultRouter()
router.register(r'donations', views.DonationsViewSet,basename='donations')

urlpatterns = (
    path('', include(router.urls)),
    )