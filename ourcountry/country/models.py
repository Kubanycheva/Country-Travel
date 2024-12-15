from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(region='KG', null=True, blank=True)


class Regions(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    regions_image = models.ImageField(upload_to='regions_image/')