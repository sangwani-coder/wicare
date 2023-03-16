from django.db import models

DONATION_CHOICES = [
    ('Health', 'Health'),
    ('Education', 'Education'),
    ('Hunger','Hunger'),
]

class Donations(models.Model):
    """
    Model that stores donations data.
    """
    created = models.DateTimeField(auto_now_add=True)
    sponsor = models.CharField(max_length=100, default='anonymous', blank=False)
    amount = models.IntegerField(blank=False)
    donate_to = models.CharField(choices=DONATION_CHOICES, default='Hunger', max_length=100)
    mobile = models.CharField(max_length=30, blank=False)
    email = models.CharField(max_length=30, blank=True)

    class Meta:
        ordering = ['created']