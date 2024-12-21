from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField


# FOR CHARLES DEO

class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(region='KG', null=True, blank=True)
    user_picture = models.ImageField(upload_to='user_pictures', null=True, blank=True)
    from_user = models.CharField(max_length=62)

# FOR HOME


class Home(models.Model):
    home_name = models.CharField(max_length=55)
    home_image = models.ImageField(upload_to='home_images', null=True, blank=True)
    home_description = models.TextField()

    def __str__(self):
        return self.home_name


class Attractions(models.Model):
    attraction_name = models.CharField(max_length=155)
    description = models.TextField()

    def __str__(self):
        return self.attraction_name

    def get_avg(self):
        return self.course_review.filter(rating=5).count()

    def get_avg_rating(self):
        ratings = self.attractions_review.all()
        if ratings.exists():
            return round(sum(i.rating for i in ratings) / ratings.count(), 1)
        return 0

    def get_rating_count(self):
        ratings = self.attractions_review.all()
        if ratings.exists():
            return ratings.count()
        return 0


class AttractionsImage(models.Model):
    attractions = models.ForeignKey(Attractions, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to='attartions_image/', null=True, blank=True)


class AttractionReview(models.Model):
    client_home = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='home_reviews')
    attractions = models.ForeignKey(Attractions, on_delete=models.CASCADE, related_name='attractions_review')
    comment = models.TextField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name='Рейтинг')

    def __str__(self):
        return f'{self.client_home}'

# FOR REGIONS


class Region(models.Model):
    region_name = models.CharField(max_length=55)
    region_image = models.ImageField(upload_to='region_images')
    region_description = models.TextField()

    def __str__(self):
        return self.region_name


class PopularPlaces(models.Model):
    popular_name = models.CharField(max_length=155)
    popular_image = models.ImageField(upload_to='popular_images')
    description = models.TextField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='popular_places')

    def __str__(self):
        return self.popular_name

    def get_avg_rating(self):
        ratings = self.popular_reviews.all()
        if ratings.exists():
            return round(sum(i.rating for i in ratings) / ratings.count(), 1)
        return 0

    def get_rating_count(self):
        ratings = self.popular_reviews.all()
        if ratings.exists():
            return ratings.count()
        return 0


class PopularReview(models.Model):
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    popular = models.ForeignKey(PopularPlaces, on_delete=models.CASCADE,  related_name='popular_reviews')
    comment = models.TextField()  #inline
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name='Рейтинг')
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.client}-{self.popular}'

    def get_static(self):
        related_reviews = PopularReview.objects.all()
        count_5 = related_reviews.filter(rating=5).count()
        count_4 = related_reviews.filter(rating=4).count()
        count_3 = related_reviews.filter(rating=3).count()
        count_2 = related_reviews.filter(rating=2).count()
        count_1 = related_reviews.filter(rating=1).count()
        return (f"exellent: {count_5} " 
                f"good: {count_4} "
                f"not bad: {count_3} "
                f"bad: {count_2} "
                f"terribly: {count_1} ")

    def get_avg_rating(self):
        ratings = PopularReview.objects.all()
        if ratings.exists():
            return round(sum(i.rating for i in ratings) / ratings.count(), 1)
        return 0

    def get_rating_count(self):
        ratings = PopularReview.objects.all()
        if ratings.exists():
            return ratings.count()
        return 0


class ReviewImage(models.Model):
    review = models.ForeignKey(PopularReview, on_delete=models.CASCADE, related_name='review_image')
    image = models.ImageField(upload_to='review_images/', null=True, blank=True)


class ToTry(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='What_to_try')
    to_name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.to_name


class ToTryImage(models.Model):
    to_try = models.ForeignKey(ToTry, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='to_try_image/', null=True, blank=True)

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

class Hotels(models.Model):
    name = models.CharField(max_length=155)
    description = models.TextField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='hotels_region')
    address = models.CharField(max_length=100)
    bedroom = models.PositiveIntegerField(default=1)
    bathroom = models.PositiveIntegerField(default=1)
    cars_bikes = models.CharField(max_length=50)
    pets = models.PositiveIntegerField()
    amenities = models.TextField()
    safety_hygiene = models.TextField()
    price_short_period = models.PositiveIntegerField()
    price_medium_period = models.PositiveIntegerField()
    price_long_period = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    def get_average_rating(self):
        ratings = self.hotel_reviews.all()
        if ratings.exists():
            return round(sum(rating.stars for rating in ratings) / ratings.count(), 1)
        return 0

    def get_rating_count(self):
        ratings = self.hotel_reviews.all()
        if ratings.exists():
            return ratings.count()
        return 0


class HotelsImage(models.Model):
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE, related_name='hotel_image')
    image = models.ImageField(upload_to='hotel_images/', null=True, blank=True)


class HotelsReview(models.Model):
    client_hotel = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='client_hotel')
    comment = models.TextField()
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE, related_name='hotel_reviews')  # inline
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)


    def __str__(self):
        return f'{self.client_hotel}'

# for kitchen


class Kitchen(models.Model):
    kitchen_name = models.CharField(max_length=155)
    description = models.TextField()
    kitchen_region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='hotels_region_image')
    price = models.PositiveIntegerField()
    specialized_menu = models.TextField()
    MEAL_TIME = (
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Brunch', 'Brunch'),
        ('Open Late', 'Open Late'),
        ('Drinks', 'Drinks'),
    )
    meal_time = MultiSelectField(choices=MEAL_TIME)
    TYPE = (
        ('Russian', 'Russian'),
        ('Asian', 'Asian'),
        ('Canadian', 'Canadian'),
        ('Chinese', 'Chinese'),
        ('European', 'European'),
        ('Japan', 'Japan'),
        ('Korean', 'Korean'),
    )
    type_of_cafe = MultiSelectField(choices=TYPE)

    def __str__(self):
        return self.kitchen_name

    def get_average_rating(self):
        ratings = self.kitchen_reviews.all()
        if ratings.exists():
            return round(sum(rating.rating for rating in ratings) / ratings.count(), 1)
        return 0

    def get_rating_count(self):
        ratings = self.kitchen_reviews.all()
        if ratings.exists():
            return ratings.count()
        return 0


class KitchenImage(models.Model):
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE, related_name='kitchen_image')
    image = models.ImageField(upload_to='kitchen_images/', null=True, blank=True)


class KitchenReview(models.Model):
    client_kitchen = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    comment = models.TextField()
    kitchen_region = models.ForeignKey(Kitchen, on_delete=models.CASCADE, related_name='kitchen_reviews')  # inline
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)

    def get_avg(self):
        return self.course_review.filter(rating=5).count()

    def __str__(self):
        return f'{self.client_kitchen}'


# FOR event
#  7 categories


class EventCategories(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category


class Event(models.Model):
    category = models.ForeignKey(EventCategories, on_delete=models.CASCADE, related_name='event_category')
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)
    title = models.CharField(max_length=52)
    date = models.DateField()
    time = models.TimeField()
    address = models.CharField(max_length=150)
    price = models.PositiveIntegerField()


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

    def get_avg(self):
        return self.course_review.filter(rating=5).count()

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


# class Kitchen(models.Model):
#     kitchen_name = models.CharField(max_length=300)
#     culture_kitchen = models.ForeignKey(Culture, on_delete=models.CASCADE, related_name='culture_kitchen')
#     kitchen_description = models.TextField()
#     kitchen_image = models.ImageField(upload_to='kitchen_images')
#
#     def __str__(self):
#         return self.kitchen_name
#


# FOR FAVORITE


class Favorite(models.Model):
    user = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='regions')
    country_favorite = models.CharField(max_length=255)

    def __str__(self):
        return self.country_favorite


class FavoriteItem(models.Model):
    favorite = models.ForeignKey(Favorite, related_name='items', on_delete=models.CASCADE)
    attractions = models.ForeignKey(Attractions, on_delete=models.CASCADE, null=True, blank=True)
    popular_region = models.ForeignKey(PopularPlaces, on_delete=models.CASCADE, null=True, blank=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, null=True, blank=True)
