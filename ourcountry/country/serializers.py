from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate


# FOR CHARLES DEO

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'user_picture', 'from_user', 'cover_photo']


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'first_name', 'last_name', 'user_picture', 'from_user']


# FOR Attraction

class AttractionsReviewImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = AttractionsImage
        fields = ['id', 'image']


class AttractionReviewListSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()
    rating_count = serializers.SerializerMethodField()
    static = serializers.SerializerMethodField()
    client_home = UserProfileSimpleSerializer(read_only=True)
    attractions = serializers.SlugRelatedField(
        queryset=Attractions.objects.all(),
        slug_field='attraction_name'
    )
    attraction_review_image = AttractionsReviewImageSerializers(read_only=True, many=True)

    class Meta:
        model = AttractionReview
        fields = ['id', 'client_home', 'static', 'attractions', 'attraction_comment', 'attraction_review_image',
                  'avg_rating', 'rating_count']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_rating_count(self, obj):
        return obj.get_rating_count()

    def get_static(self, obj):
        return obj.get_static()


class AttractionReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttractionReview
        fields = ['client_home', 'attractions', 'attraction_comment', 'rating']

    def create(self, validated_data):
        # Сначала сохраняем отзыв
        attraction_review = AttractionReview.objects.create(**validated_data)
        return attraction_review


class AttractionsImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = AttractionsImage
        fields = ['id', 'image']


class AttractionsListSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()
    rating_count = serializers.SerializerMethodField()
    region_category = serializers.SlugRelatedField(
        queryset=Region_Categoty.objects.all(),#Liliya
        slug_field='region_category'
    )

    class Meta:
        model = Attractions
        fields = ['id', 'attraction_name', 'region_category', 'main_image', 'description', 'avg_rating',
                  'rating_count', 'popular_places']

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


class PopularReviewListSerializer(serializers.ModelSerializer):
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


class PopularReviewCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = PopularReview
        fields = ['client', 'popular', 'comment', 'rating']

    def create(self, validated_data):
        # Сначала сохраняем отзыв
        popular_review_create = PopularReview.objects.create(**validated_data)
        return popular_review_create


class PopularPlacesDetailSerializer(serializers.ModelSerializer):
    popular_reviews = PopularReviewListSerializer(read_only=True, many=True)

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
        slug_field='region_category',
        queryset=Region_Categoty.objects.all()  #Liliya
    )

    class Meta:
        model = Hotels
        fields = ['id', 'name', 'main_image', 'average_rating', 'rating_count', 'region', 'popular_places']

    def get_average_rating(self, obj):
        return obj.get_average_rating()

    def get_rating_count(self, obj):
        return obj.get_rating_count()


class HotelReviewListSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()
    rating_count = serializers.SerializerMethodField()
    client_hotel = UserProfileSimpleSerializer(read_only=True)
    static = serializers.SerializerMethodField()
    hotel_review_image = HotelImageSerializers(read_only=True, many=True)

    class Meta:
        model = HotelsReview
        fields = ['client_hotel', 'hotel', 'comment', 'static', 'avg_rating', 'rating_count', 'hotel_review_image']

    def get_static(self, obj):
        return obj.get_static()

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_rating_count(self, obj):
        return obj.get_rating_count()


class HotelDetailSerializer(serializers.ModelSerializer):
    hotel_image = HotelImageSerializers(read_only=True, many=True)
    hotel_reviews = HotelReviewListSerializer(read_only=True, many=True)

    class Meta:
        model = Hotels
        fields = ['id', 'name', 'hotel_image', 'address', 'description', 'bedroom', 'bathroom', 'cars', 'bikes',
                  'pets', 'amenities', 'safety_and_hygiene', 'price_short_period',
                  'price_medium_period', 'price_long_period', 'hotel_reviews']


class HotelsReviewImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = HotelsReviewImage
        fields = ['id', 'image']


class HotelsReviewCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = HotelsReview
        fields = ['client_hotel', 'comment', 'hotel', 'rating',]

    def create(self, validated_data):
        # Сначала сохраняем отзыв
        hotel_review_create = HotelsReview.objects.create(**validated_data)
        return hotel_review_create


# FOR KITCHEN
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
    kitchen_region = serializers.SlugRelatedField(
        queryset=Region_Categoty.objects.all(),  #Liliya
        slug_field='region_category'
    )

    class Meta:
        model = Kitchen
        fields = ['id', 'kitchen_name', 'price', 'popular_places', 'kitchen_region', 'type_of_cafe', 'average_rating', 'rating_count', 'main_image']

    def get_average_rating(self, obj):
        return obj.get_average_rating()

    def get_rating_count(self, obj):
        return obj.get_rating_count()


class KitchenReviewImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = KitchenReviewImage
        fields = ['id', 'image']


class KitchenReviewListSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()
    rating_count = serializers.SerializerMethodField()
    client_kitchen = UserProfileSimpleSerializer(read_only=True)
    static = serializers.SerializerMethodField()
    kitchen_region = serializers.SlugRelatedField(
        queryset=Kitchen.objects.all(),
        slug_field='kitchen_name'
    )
    kitchen_review_image = KitchenReviewImageSerializer(read_only=True, many=True)

    class Meta:
        model = KitchenReview
        fields = ['client_kitchen', 'kitchen_region', 'comment', 'static', 'avg_rating', 'rating_count',
                  'created_at', 'kitchen_review_image']

    def get_static(self, obj):
        return obj.get_static()

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_rating_count(self, obj):
        return obj.get_rating_count()


class KitchenDetailSerializers(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    rating_count = serializers.SerializerMethodField()
    kitchen_image = KitchenImageSerializers(read_only=True, many=True)
    nutrition_rating = serializers.SerializerMethodField()
    service_rating = serializers.SerializerMethodField()
    price_rating = serializers.SerializerMethodField()
    atmosphere_rating = serializers.SerializerMethodField()
    kitchen = KitchenLocationSerializers(read_only=True, many=True)
    kitchen_reviews = KitchenReviewListSerializer(read_only=True, many=True)

    class Meta:
        model = Kitchen
        fields = ['id', 'kitchen_name', 'main_image', 'kitchen_image', 'price', 'specialized_menu', 'meal_time', 'description',
                  'average_rating', 'rating_count', 'nutrition_rating', 'service_rating', 'price_rating',
                  'atmosphere_rating', 'kitchen', 'kitchen_reviews']

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


class KitchenReviewCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = KitchenReview
        fields = ['client_kitchen', 'kitchen_region', 'comment', 'rating',
                  'nutrition_rating', 'service_rating', 'price_rating', 'atmosphere_rating']

    def create(self, validated_data):
        # Сначала сохраняем отзыв
        kitchen_review_create = KitchenReview.objects.create(**validated_data)
        return kitchen_review_create


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


#FOR CURRENCY


class Currency_DescriptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Currency_Description
        fields = ['description']


class Currency_ImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Currency_Image
        fields = ['front_image', 'back_image']


class CurrencySerializers(serializers.ModelSerializer):
    culture = CultureSimpleSerializers(read_only=True)
    currency_description = Currency_DescriptionSerializers(read_only=True, many=True)
    currency_image = Currency_ImageSerializers(read_only=True, many=True)


    class Meta:
        model = Currency
        fields = ['id',  "culture", 'currency_name', 'currency_description', 'currency_image']


class NationalInstrumentsSerializers(serializers.ModelSerializer):
    culture = CultureSimpleSerializers(read_only=True)

    class Meta:
        model = NationalInstruments
        fields = ['id',  "culture", 'national_name', 'national_description', 'national_image']


class CultureKitchenImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = CultureKitchenImage
        fields = ['id', 'image']


class CultureKitchenSerializers(serializers.ModelSerializer):
    culture = CultureSimpleSerializers(read_only=True)
    culture_kitchen_image = CultureKitchenImageSerializers(read_only=True, many=True)

    class Meta:
        model = CultureKitchen
        fields = ['id',  "culture", 'kitchen_name', 'kitchen_description', 'culture_kitchen_image']


class GalleryReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryReview
        fields = ['client_gallery', 'comment', 'gallery', 'rating']

    def create(self, validated_data):
        # Сначала сохраняем отзыв
        gallery_review_create = GalleryReview.objects.create(**validated_data)
        return gallery_review_create


class GalleryReviewImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = GalleryReviewImage
        fields = ['id', 'image']


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


# FOR USER_HISTORY_REVIEW

class AttractionReviewSerializer(serializers.ModelSerializer):
    client_home = UserProfileSimpleSerializer(read_only=True)
    attractions = serializers.SlugRelatedField(
        queryset=Attractions.objects.all(),
        slug_field='attraction_name'
    )
    attraction_review_image = AttractionsReviewImageSerializers(read_only=True, many=True)

    class Meta:
        model = AttractionReview
        fields = '__all__'


class PopularReviewSerializer(serializers.ModelSerializer):
    client = UserProfileSimpleSerializer(read_only=True)
    popular = serializers.SlugRelatedField(
        queryset=PopularPlaces.objects.all(),
        slug_field='popular_name'
    )
    review_image = ReviewImageSerializer(read_only=True, many=True)

    class Meta:
        model = PopularReview
        fields = '__all__'


class HotelsReviewSerializer(serializers.ModelSerializer):
    client_hotel = UserProfileSimpleSerializer(read_only=True)
    hotel = serializers.SlugRelatedField(
        queryset=Hotels.objects.all(),
        slug_field='name'
    )
    hotel_review_image = HotelsReviewImageSerializers(read_only=True, many=True)

    class Meta:
        model = HotelsReview
        fields = '__all__'


class KitchenReviewSerializer(serializers.ModelSerializer):
    client_kitchen = UserProfileSimpleSerializer(read_only=True)
    kitchen_region = serializers.SlugRelatedField(
        queryset=Kitchen.objects.all(),
        slug_field='kitchen_name'
    )
    kitchen_review_image = KitchenReviewImageSerializer(read_only=True, many=True)

    class Meta:
        model = KitchenReview
        fields = '__all__'


class GalleryReviewSerializer(serializers.ModelSerializer):
    client_gallery = UserProfileSimpleSerializer(read_only=True)
    gallery = serializers.SlugRelatedField(
        queryset=Gallery.objects.all(),
        slug_field='gallery_name'
    )
    gallery_review_image = GalleryReviewImageSerializers(read_only=True, many=True)

    class Meta:
        model = GalleryReview
        fields = '__all__'


class FavoriteItemSerializers(serializers.ModelSerializer):
    attractions = AttractionsListSerializer(read_only=True)
    popular_region = PopularPlacesListSerializer(read_only=True)
    gallery = GallerySerializers(read_only=True)
    hotels = HotelsListSerializer(read_only=True)

    class Meta:
        model = FavoriteItem
        fields = ['id', 'attractions', 'popular_region', 'gallery', 'hotels']


class FavoriteSerializers(serializers.ModelSerializer):
    items = FavoriteItemSerializers(read_only=True, many=True)

    class Meta:
        model = FavoriteItem
        fields = ['user', 'items']