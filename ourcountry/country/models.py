from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(region='KG', null=True, blank=True)


class Home(models.Model):
    home_name = models.CharField(max_length=25)
    home_image = models.ImageField(upload_to='home_images/', null=True, blank=True)
    description_home = models.TextField()

    def __str__(self):
        return f'{self.home_name}'


class Regions(models.Model):
    region_name = models.CharField(max_length=32)
    description_regions = models.TextField()
    regions_image = models.ImageField(upload_to='regions_images/', null=True, blank=True)

    def __str__(self):
        return self.region_name


class CountryFood(models.Model):
    regions = models.ForeignKey(Regions, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=155)
    description_food = models.TextField()
    food_image = models.ImageField(upload_to='food_images', null=True, blank=True)

    def __str__(self):
        return self.food_name


class PopularPlaces(models.Model):
    regions = models.ForeignKey(Regions, on_delete=models.CASCADE)
    places_name = models.CharField(max_length=155)
    places_image = models.ImageField(upload_to='places_images', null=True, blank=True)

    def get_avg_rating(self):
        ratings = self.regions_reviews.all()
        if ratings.exists():
            return round(sum(i.rating for i in ratings) / ratings.count(), 1)
        return 0

    def __str__(self):
        return self.places_name


class PopularReview(models.Model):
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    regions = models.ForeignKey(Regions, on_delete=models.CASCADE, related_name='regions_reviews')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()

    def __str__(self):
        return f'{self.rating} - {self.client}'


class Concert(models.Model):
    concert_name = models.CharField(max_length=155, unique=True)

    def __str__(self):
        return self.concert_name