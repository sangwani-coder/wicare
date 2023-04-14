# models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from .choices import ModelChoices as md

PROVINCE_UNKNOWN = '....'

def upload_to(instance, filename):
    return 'user_profile_image/{}/{}'.format(instance.user_id, filename)


class UserProfile(models.Model):
    # gender choices
    GENDER_UNKNOWN = 'U'
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_CHOICES = (
        (GENDER_UNKNOWN, _('unknown')),
        (GENDER_MALE, _('male')),
        (GENDER_FEMALE, _('female')),
    )
    
    user = models.OneToOneField(
        User, related_name="profile", on_delete=models.CASCADE)
    gender = models.CharField(_('gender'),
        max_length=1, choices=GENDER_CHOICES, default=GENDER_UNKNOWN)
    user_profile = models.CharField(_('user_profile'),
        max_length=10, choices=md.USER_PROFILE_CHOICES, default=md.DEFAULT)
    is_nurse = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_donor = models.BooleanField(default=False)
    phone_number = PhoneNumberField(_('phone number'), blank=True)
    account_number = models.CharField(max_length=20, blank=True)
    location = models.CharField(_('location'),
        max_length=15, choices=md.ZAMBIAN_PROVINCE_CHOICES,
        default=PROVINCE_UNKNOWN, blank=True)
    bio = models.TextField(max_length=150)
    image = models.ImageField(_('image'),
        blank=True, null=True, upload_to=upload_to)


class Donee(models.Model):
    user = models.ForeignKey(User, related_name="donees", on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    location = models.CharField(_('location'),
        max_length=15, choices=md.ZAMBIAN_PROVINCE_CHOICES,
        default=PROVINCE_UNKNOWN, blank=True)
    image = models.ImageField(_('image'), blank=True, null=True, upload_to=upload_to)
    need = models.TextField()
    bio = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.full_name + ', ' + self.location[1] + ', ' + self.need


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