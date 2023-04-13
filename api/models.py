# models.py
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    is_nurse = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    identification_type = models.CharField(max_length=10)
    identification_number = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=20)
    account_number = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    bio = models.TextField()


class DonorProfile(models.Model):
    user = models.OneToOneField(User, related_name="donor_profile", on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    is_monthly_donor = models.BooleanField(default=False)
    bio = models.TextField()


class Donee(models.Model):
    user = models.ForeignKey(User, related_name="donees", on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    need = models.TextField()
    bio = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.full_name + ', ' + self.location + ', ' + self.need


class Donation(models.Model):
    donee = models.ForeignKey(Donee, related_name="donation", on_delete=models.CASCADE)
    donor_full_names = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    amount = models.FloatField()
    comment = models.TextField()
    account_number = models.CharField(max_length=36)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.donor_full_names