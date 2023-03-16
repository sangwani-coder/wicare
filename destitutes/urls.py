from django.urls import path, include
from rest_framework.routers import DefaultRouter
from destitutes import views

router = DefaultRouter()

router.register(r'destitutes', views.DestitutesViewSet,basename='destitutes')

urlpatterns = [
    path('', include(router.urls)),
]