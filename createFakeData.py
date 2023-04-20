import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wicare.settings')
django.setup()

from django.utils import timezone
from faker import Faker
import random
import os


from api import choices
from api import choices

# Instantiate Faker object
fake = Faker()

def create_fake_data():
    # Create some fake Users to associate with the Donee objects
    from django.contrib.auth.models import User
    from api.models import Donee, Donation

    users = []
    for i in range(10):
        username = f"user{i}"
        email = fake.email()
        password = fake.password()
        user = User.objects.create_user(username=username, email=email, password=password)
        users.append(user)

    # Define the choices for the 'cause' field
    causes = [choice[0] for choice in choices.CAUSES_CHOICES]

    # Define the choices for the 'location' field
    locations = [choice[0] for choice in choices.ZAMBIAN_PROVINCE_CHOICES]

    # Create some fake Donee objects
    for i in range(50):
        # Choose a random User as the foreign key
        user = random.choice(users)

        # Generate fake data for the other fields
        full_name = fake.name()
        location = random.choice(locations)
        need = fake.text()
        bio = fake.text()
        amount_needed = fake.random_int(min=50, max=1000)
        cause = random.choice(causes)
        date_created = fake.date_time_between(start_date='-1y', end_date='now', tzinfo=timezone.get_current_timezone())

        # Create the Donee object
        donee = Donee.objects.create(
            user=user,
            full_name=full_name,
            location=location,
            need=need,
            bio=bio,
            amount_needed=amount_needed,
            cause=cause,
            date_created=date_created,
        )

        # # Optionally, add a random image
        # if fake.boolean(chance_of_getting_true=50):
        #     image_filename = fake.file_name(extension='jpg')
        #     image_path = os.path.join('donee_images', image_filename)
        #     donee.image.save(image_filename, fake.binary(), save=True)


    # Create fake donation data
    for i in range(10):
        donor_full_names = fake.name()
        location = random.choice(choices.ZAMBIAN_PROVINCE_CHOICES)[0]
        amount_donated = random.uniform(10, 1000)
        comment = fake.text()
        account_number = fake.random_int(100000000, 999999999)
        cause = random.choice(choices.CAUSES_CHOICES)[0]
        date_created = fake.date_this_month(before_today=True, after_today=False)

        # Create the Donation object
        donation = Donation.objects.create(
            cause=cause,
            donor_full_names=donor_full_names,
            location=location,
            amount_donated=amount_donated,
            comment=comment,
            account_number=account_number,
            date_created=date_created,
        )
    print('Models Mocked Successfully')

if __name__=="__main__":
    create_fake_data()