from django.db import models

class DestitutesEducation(models.Model):
    """
    Model that stores childs data.
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

class DestitutesHealth(models.Model):
    """
    Model that stores a patients data.
    """
    created = models.DateTimeField(auto_now_add=True)
    patientsnames = models.CharField(max_length=100, blank=False)
    patientsage = models.IntegerField(blank=False)
    patientsphoto =  models.ImageField(blank=True)
    hospital = models.CharField(max_length=100, blank=False)
    medicalcondition = models.TextField(max_length=1000)
    requiredfunds = models.IntegerField(blank=False)
    requiredtreatment = models.CharField(max_length=150, blank=False)
    urgent = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']
