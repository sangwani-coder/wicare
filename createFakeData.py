import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "helloworld.settings")

import django 
django.setup() 

from faker import factory,Faker 
from api.models import * 
from model_bakery.recipe import Recipe,foreign_key
from django.contrib.auth.models import User

fake = Faker() 

for k in range(100):
    user=Recipe(User,
                username=fake.name(),
                email=fake.email(),
                password=fake.password())
  
    donee=Recipe(Donee, 
                user = foreign_key(user)
                full_name = fake
                location = models.CharField(_('location'),
                    max_length=15, choices=md.ZAMBIAN_PROVINCE_CHOICES,
                    default=PROVINCE_UNKNOWN, blank=True)
                image = models.ImageField(_('image'), blank=True, null=True, upload_to=upload_to)
                need = fake.text()
                bio = fake.text()
                amount_needed = fake
                cause = models.CharField(_('cause'),
                    max_length=20, choices=CAUSES_CHOICES, default=CAUSE_GENERAL, blank=False)
                date_created = fake.future_datetime(end_date="+30d",tzinfo=None),)
    
    donation = Recipe(Donation, 
                cause = models.CharField(_('cause'),
                    max_length=20, choices=CAUSES_CHOICES, default=CAUSE_GENERAL, blank=True)
                donor_full_names = fake.name()
                location = fake
                amount_donated = fake
                comment = fake.text()
                account_number = fake
                date_created = fake.future_datetime(end_date="+30d",tzinfo=None),)

    donation.make()