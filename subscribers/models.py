from django.db import models

LOCATION_CHOICES = [
    ('Copperbelt','Copperbelt'),
    ('Lusaka','Lusaka'),
    ('Central','Central'),
    ('North Western','North Western'),
    ('Luapula','Luapula'),
    ('Southern','Southern'),
    ('Eastern','Eastern'),
    ('Western','Western'),
    ('Muchinga','Muchinga'),
    ('Nothern','Northern'),
    ]

# Create your models here.
class Subscribers(models.Model):
    """
    Model that stores Subscribers details.
    """
    created = models.DateTimeField(auto_now_add=True)
    firstname = models.CharField(max_length=30, blank=False)
    lastname = models.CharField(max_length=30, blank=False)
    location = models.CharField(choices=LOCATION_CHOICES, max_length=100)
    mobile = models.CharField(max_length=30, blank=False)
    email = models.CharField(max_length=30, blank=False)
    owner = models.ForeignKey('auth.User', related_name='subscribers', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
