from django.db import models

class Destitutes(models.Model):
    """
    Model that stores destitutes data.
    """
    created = models.DateTimeField(auto_now_add=True)
    caregiver = models.ForeignKey('auth.User', related_name='caregiver', on_delete=models.CASCADE)
    familyname = models.CharField(max_length=100, blank=False)
    shortstory = models.CharField(max_length=250)
    problemdescription = models.TextField(max_length=1000)
    image =  models.ImageField(blank=True)
    monthlybudget = models.IntegerField(blank=False)

    class Meta:
        ordering = ['created']