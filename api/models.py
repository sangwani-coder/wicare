# models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from . import choices

def upload_to(instance, filename):
    return 'user_profile_image/{}/{}'.format(instance.user_id, filename)


class UserProfile(models.Model):
    
    user = models.OneToOneField(
        User, related_name="profile", on_delete=models.CASCADE)
    gender = models.CharField(_('gender'),
        max_length=10, choices=choices.GENDER_CHOICES, default='unknown')
    user_profile = models.CharField(_('user_profile'),
        max_length=30, choices=choices.USER_PROFILE_CHOICES, default='donor')
    is_nurse = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_donor = models.BooleanField(default=False)
    phone_number = PhoneNumberField(_('phone number'), blank=True)
    account_number = models.CharField(max_length=20, blank=True)
    location = models.CharField(_('location'),
        max_length=50, choices=choices.ZAMBIAN_PROVINCE_CHOICES,
        default='central province', blank=True)
    bio = models.TextField(max_length=150)
    image = models.ImageField(_('image'),
        blank=True, null=True, upload_to=upload_to)


class Donee(models.Model):
    user = models.ForeignKey(User, related_name="donees", on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    location = models.CharField(_('location'),
        max_length=50, choices=choices.ZAMBIAN_PROVINCE_CHOICES,
        default='central province',
        blank=False)
    image = models.ImageField(_('image'), blank=True, null=True, upload_to=upload_to)
    need = models.TextField()
    bio = models.TextField()
    amount_needed = models.IntegerField(default=350)
    cause = models.CharField(_('cause'),
        max_length=50, choices=choices.CAUSES_CHOICES, default='general', blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.full_name + ', ' + self.location[1] + ', ' + self.need

def get_default_donee():
    """
    get a default value for Donation Donee, create new status if not available.
    """
    user = User.objects.first()
    return Donee.objects.get_or_create(
        user = user,
        full_name="wicare-general",
        need = "Help the needy in society",
        bio = "Wicare connects the poor with individuals willing to help"
        )[0]

class Donation(models.Model):
    cause = models.CharField(_('cause'),
        max_length=50, choices=choices.CAUSES_CHOICES, default='general', blank=True)
    donor_full_names = models.CharField(max_length=255)
    location = models.CharField(_('location'),
        max_length=50, choices=choices.ZAMBIAN_PROVINCE_CHOICES,
        default='central province',
        blank=False)
    amount_donated = models.IntegerField()
    comment = models.TextField(blank=True)
    account_number = models.CharField(max_length=15)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.donor_full_names