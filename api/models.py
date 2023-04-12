# models.py
from django.db import models
from django.contrib.auth.models import User

class Donee(models.Model):
    user = models.ForeignKey(User, related_name="donees", on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    need = models.TextField()
    bio = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.full_name + ', ' + self.location + ', ' + self.need