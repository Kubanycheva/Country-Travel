from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


# FOR CHARLES DEO


class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(region='KG', null=True, blank=True)
    user_picture = models.ImageField(upload_to='user_pictures', null=True, blank=True)


# FOR HOME


class Home(models.Model):
    home_name = models.CharField(max_length=55)
    home_image = models.ImageField(upload_to='home_images')
    home_description = models.TextField()

    def __str__(self):
        return self.home_name


class AttractionsHome(models.Model):
    attraction_name = models.CharField(max_length=155)
    attraction_image = models.ImageField(upload_to='attraction_images')
    description = models.TextField()
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='attractions_home')

    def __str__(self):
        return self.attraction_name


class HomeReview(models.Model):
    client_home = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='home_reviews')
    attractions_home = models.ForeignKey(AttractionsHome, on_delete=models.CASCADE, related_name='attractions_home')
    comment = models.TextField()
    home = models.ForeignKey(Home, on_delete=models.CASCADE)  #inline

    def __str__(self):
        return f'{self.client_home}'

    def get_avg_rating(self):
        ratings = self.home_reviews.all()
        if ratings.exists():
            return round(sum(i.rating for i in ratings) / ratings.count(), 1)
        return 0


class AttractionCulture(models.Model):
    a_name = models.CharField(max_length=200)
    description = models.TextField()
    a_image = models.ImageField(upload_to='a_images')

    def __str__(self):
        return self.a_name


# FOR REGIONS


class Region(models.Model):
    region_name = models.CharField(max_length=55)
    region_image = models.ImageField(upload_to='region_images')
    region_description = models.TextField()

    def __str__(self):
        return self.region_name


class PopularRegion(models.Model):
    popular_name = models.CharField(max_length=155)
    popular_image = models.ImageField(upload_to='popular_images')
    description = models.TextField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='popular_region')

    def __str__(self):
        return self.popular_name


class PopularReview(models.Model):
    client_popular = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='popular_reviews')
    comment = models.TextField()
    popular = models.ForeignKey(PopularRegion, on_delete=models.CASCADE)  #inline

    def __str__(self):
        return f'{self.client_popular}'

    def get_avg_rating(self):
        ratings = self.popular_reviews.all()
        if ratings.exists():
            return round(sum(i.rating for i in ratings) / ratings.count(), 1)
        return 0


class ToTry(models.Model):
    to_name = models.CharField(max_length=200)
    description = models.TextField()
    to_image = models.ImageField(upload_to='to_images')

    def __str__(self):
        return self.to_name


# FOR GALLERY

class Gallery(models.Model):
    gallery_name = models.CharField(max_length=55)
    gallery_image = models.ImageField(upload_to='gellery_images')

    def __str__(self):
        return self.gallery_name


class GalleryReview(models.Model):
    client_gallery = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='gallery_reviews')
    comment = models.TextField()
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE) #inline

    def __str__(self):
        return f'{self.client_gallery}'

    def get_avg_rating(self):
        ratings = self.gallery_reviews.all()
        if ratings.exists():
            return round(sum(i.rating for i in ratings) / ratings.count(), 1)
        return 0


# FOR CULTURE


class Culture(models.Model):
    culture_name = models.CharField(max_length=35)
    culture_description = models.TextField()
    culture_image = models.ImageField(upload_to='culture-images')

    def __str__(self):
        return self.culture_name


class Games(models.Model):
    games_name = models.CharField(max_length=300)
    culture_games = models.ForeignKey(Culture, on_delete=models.CASCADE, related_name='culture_games')
    games_description = models.TextField()
    games_image = models.ImageField(upload_to='games_images')

    def __str__(self):
        return self.games_name


class NationalClothes(models.Model):
    clothes_name = models.CharField(max_length=300)
    culture_clothes = models.ForeignKey(Culture, on_delete=models.CASCADE, related_name='culture_clothes')
    clothes_description = models.TextField()
    clothes_image = models.ImageField(upload_to='clothes_images')

    def __str__(self):
        return self.clothes_name


class HandCrafts(models.Model):
    hand_name = models.CharField(max_length=300)
    culture_hand = models.ForeignKey(Culture, on_delete=models.CASCADE, related_name='culture_hand')
    hand_description = models.TextField()
    hand_image = models.ImageField(upload_to='hand_images')

    def __str__(self):
        return self.hand_name


class Currency(models.Model):
    currency_name = models.CharField(max_length=300)
    culture_currency = models.ForeignKey(Culture, on_delete=models.CASCADE, related_name='culture_currency')
    currency_description = models.TextField()
    hand_image = models.ImageField(upload_to='currency_images')

    def __str__(self):
        return self.currency_name


class NationalInstruments(models.Model):
    national_name = models.CharField(max_length=300)
    culture_national = models.ForeignKey(Culture, on_delete=models.CASCADE, related_name='culture_national')
    national_description = models.TextField()
    national_image = models.ImageField(upload_to='national_images')

    def __str__(self):
        return self.national_name


class Kitchen(models.Model):
    kitchen_name = models.CharField(max_length=300)
    culture_kitchen = models.ForeignKey(Culture, on_delete=models.CASCADE, related_name='culture_kitchen')
    kitchen_description = models.TextField()
    kitchen_image = models.ImageField(upload_to='kitchen_images')

    def __str__(self):
        return self.kitchen_name


# FOR FIVE_CATEGORIES

# for places


class PlacesRegion(models.Model):
    user_name = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField(null=True, blank=True)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user_name

    def get_avg_rating(self):
        ratings = self.reviews.all()
        if ratings.exists():
            return round(sum(i.rating for i in ratings) / ratings.count(), 1)
        return 0


# FOR Hotels


class HotelsRegion(models.Model):
    hotels_region_name = models.CharField(max_length=155)
    hotels_region_image = models.ImageField(upload_to='hotels_region_images')
    description = models.TextField()
    hotels_region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='hotels_region')

    def __str__(self):
        return self.hotels_region_name


class HotelsReview(models.Model):
    client_hotel = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='hotels_region_reviews')
    comment = models.TextField()
    hotel_region = models.ForeignKey(HotelsRegion, on_delete=models.CASCADE)  # inline

    def __str__(self):
        return f'{self.client_hotel}'

    def get_average_rating(self):
        ratings = self.hotels_region_reviews.all()
        if ratings.exists():
            return round(sum(rating.stars for rating in ratings) / ratings.count(), 1)
        return 0


# for kitchen


class Kitchen(models.Model):
    kitchen_name = models.CharField(max_length=155)
    kitchen_image = models.ImageField(upload_to='kitchen_images')
    description = models.TextField()
    kitchen_region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='hotels_region_image')

    def __str__(self):
        return self.kitchen_name


class KitchenReview(models.Model):
    client_kitchen = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='kitchen_reviews')
    comment = models.TextField()
    kitchen_region = models.ForeignKey(Kitchen, on_delete=models.CASCADE)  # inline

    def __str__(self):
        return f'{self.client_kitchen}'

    def get_average_rating(self):
        ratings = self.kitchen_reviews.all()
        if ratings.exists():
            return round(sum(rating.stars for rating in ratings) / ratings.count(), 1)
        return 0


# FOR event

#  7 categories

class Concert(models.Model):
    concert_name = models.CharField(max_length=16, unique=True)    #concert

    def __str__(self):
        return self.concert_name


class EventConcert(models.Model):
    title_concert = models.CharField(max_length=150)
    created_date = models.DateTimeField(auto_now_add=True)
    text_concert = models.CharField(max_length=155)
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title_concert


class Cinema(models.Model):
    cinema_name = models.CharField(max_length=16, unique=True) #Cinema

    def __str__(self):
        return self.cinema_name


class EventCinema(models.Model):
    title_cinema = models.CharField(max_length=150)
    created_date = models.DateTimeField(auto_now_add=True)
    text_cinema = models.CharField(max_length=155)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title_cinema


class Leisure(models.Model):
    leisure_name = models.CharField(max_length=16, unique=True)  #Leisure

    def __str__(self):
        return self.leisure_name


class EventLeisure(models.Model):
    title_leisure = models.CharField(max_length=150)
    created_date = models.DateTimeField(auto_now_add=True)
    text_leisure = models.CharField(max_length=155)
    leisure = models.ForeignKey(Leisure, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title_leisure


class Theater(models.Model):
    theater_name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.theater_name


class EventTheater(models.Model):
    title_theater = models.CharField(max_length=150)
    created_date = models.DateTimeField(auto_now_add=True)
    text_theater = models.CharField(max_length=155)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title_theater


class MasterClasses(models.Model):
    master_name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.master_name


class EventMaster(models.Model):
    title_master = models.CharField(max_length=150)
    created_date = models.DateTimeField(auto_now_add=True)
    text_master = models.CharField(max_length=155)
    master_classes = models.ForeignKey(MasterClasses, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title_master


class Tourism(models.Model):
    tourism_name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.tourism_name


class EventTourism(models.Model):
    tourism_master = models.CharField(max_length=150)
    created_date = models.DateTimeField(auto_now_add=True)
    text_tourism = models.CharField(max_length=155)
    tourism = models.ForeignKey(Tourism, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.tourism_master

#FOR Attractions


class AttractionsEvent(models.Model):
    attraction_event = models.CharField(max_length=155)
    attraction_event_image = models.ImageField(upload_to='attraction_event_images')
    description = models.TextField()

    def __str__(self):
        return self.attraction_event


class AttractionsEventReview(models.Model):
    client_event = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='event_reviews')
    attractions_event = models.ForeignKey(AttractionsEvent, on_delete=models.CASCADE, related_name='attractions_event')
    comment = models.TextField()
    attractions_events = models.ForeignKey(AttractionsEvent, on_delete=models.CASCADE)  #inline

    def __str__(self):
        return f'{self.client_event}'

    def get_avg_rating(self):
        ratings = self.event_reviews.all()
        if ratings.exists():
            return round(sum(i.rating for i in ratings) / ratings.count(), 1)
        return 0


# FOR FAVORITE


class Favorite(models.Model):
    user = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='regions')
    country_favorite = models.CharField(max_length=255)

    def __str__(self):
        return self.country_favorite


class FavoriteItem(models.Model):
    favorite = models.ForeignKey(Favorite, related_name='items', on_delete=models.CASCADE)
    attractions = models.ForeignKey(AttractionsHome, on_delete=models.CASCADE, null=True, blank=True)
    popular_region = models.ForeignKey(PopularRegion, on_delete=models.CASCADE, null=True, blank=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, null=True, blank=True)
    popular_region = models.ForeignKey(PopularRegion, on_delete=models.CASCADE, null=True, blank=True)



