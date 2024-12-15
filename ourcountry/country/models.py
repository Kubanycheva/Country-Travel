from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(region='KG', null=True, blank=True)

class Home(models.Model):
    name = models.CharField(max_length=25)
    image = models.ImageField(upload_to='home_image/', null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Regions(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    regions_image = models.ImageField(upload_to='regions_image/')

xdrcftvgybhunji
xdfghjk
fvghbjkhbjnk
hbjnk
asdsf
afdsv