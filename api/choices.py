"""
Defines Constants for models choice fields.
"""
from django.utils.translation import gettext_lazy as _

PROVINCE_UNKNOWN = '....'
CNT = 'Central Province'
CBT = 'Copperbelt Province'
EST = 'Eastern Province'
LPA = 'Luapula Province'
LSK = 'Lusaka Province'
MCG = 'Muchinga Province'
NTN = 'Northern Province'
NWN = 'North-Western Province'
STN = 'Southern Province'
WSN = 'Western Province'

class ModelChoices:
    """
    Defines constants for models choice fields
    """
    
    # Zambian provinces choices
    ZAMBIAN_PROVINCE_CHOICES = (
            (PROVINCE_UNKNOWN, _('unknown')),
            ('CTL', _(CNT)),
            ('CB', _(CBT)),
            ('ETN', _(EST)),
            ('LPA', _(LPA)),
            ('LSK', _(LSK)),
            ('MCG', _(MCG)),
            ('NTN', _(NTN)),
            ('NWN', _(NWN)),
            ('STN', _(STN)),
            ('WSN', _(WSN)),
        )

    # gender choices
    GENDER_UNKNOWN = 'U'
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_CHOICES = (
        (GENDER_UNKNOWN, _('unknown')),
        (GENDER_MALE, _('male')),
        (GENDER_FEMALE, _('female')),
    )

    # User type choices
    DEFAULT = 'donor'
    SUBSCRIBER = 'Subscriber'
    DONOR = 'Donor'
    USER_PROFILE_CHOICES = (
        (DEFAULT, _('donor')),
        (SUBSCRIBER, _('subscriber')),
        (DONOR, _('donor')),
    )
