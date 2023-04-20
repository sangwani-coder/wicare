"""
Defines Constants for models choice fields.
"""
from django.utils.translation import gettext_lazy as _

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

# Zambian provinces choices
ZAMBIAN_PROVINCE_CHOICES = (
        (CNT, _(CNT)),
        (CBT, _(CBT)),
        (EST, _(EST)),
        (LPA, _(LPA)),
        (LSK, _(LSK)),
        (MCG, _(MCG)),
        (NTN, _(NTN)),
        (NWN, _(NWN)),
        (STN, _(STN)),
        (WSN, _(WSN)),
    )


CAUSES_CHOICES = (
    ('general', _('general')),
    ('no poverty', _('no poverty')),
    ('zero hunger', _('zero hunger')),
    ('health and well-being.', _('health and well-being.')),
    ('quality education for all.', _('quality education for all.')),
    ('clean water and sanitation.', _('clean water and sanitation.')),
)

# gender choices
GENDER_CHOICES = (
    ('unknown', _('unknown')),
    ('male', _('male')),
    ('female', _('female')),
)

# User type choices
USER_PROFILE_CHOICES = (
    ('donor', _('donor')),
    ('subscriber', _('subscriber')),
)
