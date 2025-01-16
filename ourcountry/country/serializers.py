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
        fields = ['id', 'name', 'hotel_image', 'address', 'description', 'bedroom', 'bathroom', 'cars', 'bikes',
                  'pets', 'amenities', 'safety_and_hygiene', 'price_short_period',
                  'price_medium_period', 'price_long_period']


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