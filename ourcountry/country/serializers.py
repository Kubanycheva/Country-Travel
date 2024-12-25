from rest_framework import serializers
from .models import *

# FOR CHARLES DEO


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'first_name', 'last_name', 'user_picture', 'from_user']


# FOR Attraction
class AttractionReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttractionReview
        fields = ['id', 'avg_rating', 'rating_count']


class AttractionsImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = AttractionsImage
        fields = ['id', 'image']


class AttractionsListSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()
    rating_count = serializers.SerializerMethodField()

    class Meta:
        model = Attractions
        fields = ['id', 'attraction_name', 'main_image', 'description', 'avg_rating', 'rating_count']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_rating_count(self, obj):
        return obj.get_rating_count()


class AttractionsDetailSerializer(serializers.ModelSerializer):
    rating_count = serializers.SerializerMethodField()
    image = AttractionsImageSerializers(read_only=True, many=True)

    class Meta:
        model = Attractions
        fields = ['id', 'attraction_name', "main_image", 'image', 'description', 'rating_count']

    def get_rating_count(self, obj):
        return obj.get_rating_count()


class HomeSerializer(serializers.ModelSerializer):
    attractions_home = AttractionsListSerializer(read_only=True, many=True)

    class Meta:
        model = Home
        fields = ['id', 'home_name', 'home_image', 'home_description', 'attractions_home']


# FOR REGIONS


class PopularPlacesListSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()
    rating_count = serializers.SerializerMethodField()
    region = serializers.SlugRelatedField(
        slug_field='region_name',
        queryset=Region.objects.all()
    )

    class Meta:
        model = PopularPlaces
        fields = ['id', 'popular_name', 'popular_image', 'avg_rating', 'rating_count', 'region']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_rating_count(self, obj):
        return obj.get_rating_count()


class ToTrySerializer(serializers.ModelSerializer):

    class Meta:
        model = ToTry
        fields = ['id', 'to_name', 'first_description', 'second_description', 'image']


class ReviewImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewImage
        fields = ['id', 'image']


class RegionSerializer(serializers.ModelSerializer):
    popular_places = PopularPlacesListSerializer(read_only=True, many=True)
    What_to_try = ToTrySerializer(read_only=True, many=True)
    region_category = serializers.SlugRelatedField(
        slug_field='region_category',
        queryset=Region_Categoty.objects.all()

    )

    class Meta:
        model = Region
        fields = ['id', 'region_name', 'region_image', 'region_description', 'What_to_try', 'popular_places', 'region_category']


class PopularReviewSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()
    rating_count = serializers.SerializerMethodField()
    static = serializers.SerializerMethodField()
    client = UserProfileSimpleSerializer(read_only=True)
    review_image = ReviewImageSerializer(read_only=True, many=True)

    class Meta:
        model = PopularReview
        fields = ['id', 'client', 'created_date', 'comment', 'static', 'avg_rating', 'rating_count', 'review_image']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_rating_count(self, obj):
        return obj.get_rating_count()

    def get_static(self, obj):
        return obj.get_static()


class PopularPlacesDetailSerializer(serializers.ModelSerializer):
    popular_reviews = PopularReviewSerializer(read_only=True, many=True)

    class Meta:
        model = PopularPlaces
        fields = ['id', 'popular_name', 'popular_image', 'description', 'popular_reviews']

# FOR Hotels


class HotelImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = HotelsImage
        fields = ['id', 'image']


class HotelsListSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    rating_count = serializers.SerializerMethodField()
    region = serializers.SlugRelatedField(
        slug_field='region_name',
        queryset=Region.objects.all()
    )
    popular_places = serializers.SlugRelatedField(
        slug_field='popular_name',
        queryset=PopularPlaces.objects.all()
    )

    class Meta:
        model = Hotels
        fields = ['id', 'name', 'main_image', 'average_rating', 'rating_count', 'region', 'popular_places']

    def get_average_rating(self, obj):
        return obj.get_average_rating()

    def get_rating_count(self, obj):
        return obj.get_rating_count()


class HotelDetailSerializer(serializers.ModelSerializer):
    hotel_image = HotelImageSerializers(read_only=True, many=True)

    class Meta:
        model = Hotels
        fields = ['id', 'name', 'hotel_image', 'address', 'bedroom', 'bathroom', 'cars', 'bikes',
                  'pets', 'amenities', 'safety_and_hygiene', 'price_short_period',
                  'price_medium_period', 'price_long_period']


class HotelsReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelsReview
        fields = '__all__'


# For Kitchen
class KitchenImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = KitchenImage
        fields = ['id', 'image']


class KitchenLocationSerializers(serializers.ModelSerializer):
    kitchen = serializers.SlugRelatedField(
        slug_field='kitchen_name',
        queryset=Kitchen.objects.all()
    )

    class Meta:
        model = KitchenLocation
        fields = ['id', 'address', 'Website', "email", 'phone_number', 'kitchen']


class KitchenListSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    rating_count = serializers.SerializerMethodField()

    class Meta:
        model = Kitchen
        fields = ['id', 'kitchen_name', 'price', 'type_of_cafe', 'average_rating', 'rating_count', 'main_image']

    def get_average_rating(self, obj):
        return obj.get_average_rating()

    def get_rating_count(self, obj):
        return obj.get_rating_count()


class KitchenDetailSerializers(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    rating_count = serializers.SerializerMethodField()
    kitchen_image = KitchenImageSerializers()
    nutrition_rating = serializers.SerializerMethodField()
    service_rating = serializers.SerializerMethodField()
    price_rating = serializers.SerializerMethodField()
    atmosphere_rating = serializers.SerializerMethodField()
    kitchen = KitchenLocationSerializers(read_only=True, many=True)

    class Meta:
        model = Kitchen
        fields = ['id', 'kitchen_name', 'main_image', 'kitchen_image', 'price', 'specialized_menu', 'meal_time', 'description',
                  'average_rating', 'rating_count', 'nutrition_rating', 'service_rating', 'price_rating',
                  'atmosphere_rating', 'kitchen']

    def get_average_rating(self, obj):
        return obj.get_average_rating()

    def get_rating_count(self, obj):
        return obj.get_rating_count()

    def get_nutrition_rating(self, obj):
        return obj.get_nutrition_rating()

    def get_service_rating(self, obj):
        return obj.get_service_rating()

    def get_price_rating(self, obj):
        return obj.get_price_rating()

    def get_atmosphere_rating(self, obj):
        return obj.get_atmosphere_rating()


class KitchenReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = KitchenReview
        fields = '__all__'


class EventCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = EventCategories
        fields = ['id', 'category']


class EventSerializers(serializers.ModelSerializer):
    category = EventCategorySerializers(read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'title', 'image', 'category', 'date', 'time', 'address', 'price']


class CultureSerializers(serializers.ModelSerializer):
    class Meta:
        model = Culture
        fields = ['id', 'culture_name', 'culture_description', 'culture_image']


class CultureSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = CultureCategory
        fields = ['id', 'culture_name']


class GamesSerializers(serializers.ModelSerializer):
    culture = CultureSimpleSerializers(read_only=True)

    class Meta:
        model = Games
        fields = ['id', "culture", 'games_name', 'games_description', 'games_image']


class NationalClothesSerializers(serializers.ModelSerializer):
    class Meta:
        model = NationalClothes
        fields = ['id', "culture", 'clothes_name', 'clothes_description', 'clothes_image']


class HandCraftsSerializers(serializers.ModelSerializer):
    culture = CultureSimpleSerializers(read_only=True)

    class Meta:
        model = HandCrafts
        fields = ["id", 'culture', 'hand_name', 'hand_description', 'hand_image']


class CurrencySerializers(serializers.ModelSerializer):
    culture = CultureSimpleSerializers(read_only=True)

    class Meta:
        model = Currency
        fields = ['id',  "culture", 'currency_name', 'currency_description', 'hand_image']


class NationalInstrumentsSerializers(serializers.ModelSerializer):
    culture = CultureSimpleSerializers(read_only=True)

    class Meta:
        model = NationalInstruments
        fields = ['id',  "culture", 'national_name', 'national_description', 'national_image']


class CultureKitchenSerializers(serializers.ModelSerializer):
    culture = CultureSimpleSerializers(read_only=True)

    class Meta:
        model = CultureKitchen
        fields = ['id',  "culture", 'kitchen_name', 'kitchen_description', 'kitchen_image']


class GallerySerializers(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()
    rating_count = serializers.SerializerMethodField()

    class Meta:
        model = Gallery
        fields = ['id', 'gallery_name', 'gallery_image', 'address', 'avg_rating', 'rating_count']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_rating_count(self, obj):
        return obj.get_rating_count()
