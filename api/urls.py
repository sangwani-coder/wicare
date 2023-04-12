from django.urls import path
from .views import DoneeList, DoneeDetail

urlpatterns = [
    path('donees/', DoneeList.as_view(), name="donee_list"),
    path('donees/<int:pk>/', DoneeDetail.as_view(), name="donee_detail"),
]
