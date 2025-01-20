from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets, generics, status
from django_filters.rest_framework import DjangoFilterBackend
from .filters import *
from rest_framework.response import Response
from django.db.models import Avg, Case, When, Value, IntegerField

# FOR CHARLES DEO


class UserProfileCreateAPIView(generics.UpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

# FOR HOME


class HomeListAPIView(generics.ListAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer


class AttractionsListAPIView(generics.ListAPIView):
    queryset = Attractions.objects.all()
    serializer_class = AttractionsListSerializer


class AttractionsDetailAPIView(generics.RetrieveAPIView):
    queryset = Attractions.objects.all()
    serializer_class = AttractionsDetailSerializer


class AttractionReviewListAPIView(generics.ListAPIView):
    queryset = AttractionReview.objects.all()
    serializer_class = AttractionReviewListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AttractionReviewFilter


class AttractionReviewCreateAPIView(generics.CreateAPIView):
    queryset = AttractionReview.objects.all()
    serializer_class = AttractionReviewCreateSerializer

    def perform_create(self, serializer):
        # Сначала создаем отзыв
        attraction_review = serializer.save()

        # Если есть изображения, сохраняем их
        images = self.request.FILES.getlist('images')
        for image in images:
            AttractionsReviewImage.objects.create(attractions=attraction_review, image=image)

        return attraction_review

    def post(self, request, *args, **kwargs):
        # Используем CreateAPIView для обработки POST-запроса
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Сначала сохраняем отзыв
            attraction_review = self.perform_create(serializer)

            # Получаем сериализованные данные для ответа, включая изображения
            response_serializer = AttractionReviewSerializer(attraction_review)

            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# FOR REGIONS


class RegionListAPIView(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class PopularPlacesListAPI(generics.ListAPIView):
    queryset = PopularPlaces.objects.all()
    serializer_class = PopularPlacesListSerializer


class PopularPlacesDetailAPI(generics.RetrieveAPIView):
    queryset = PopularPlaces.objects.all()
    serializer_class = PopularPlacesDetailSerializer


class PopularReviewListAPIView(generics.ListAPIView):
    queryset = PopularReview.objects.all()
    serializer_class = PopularReviewListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PopularReviewFilter


class PopularReviewCreateAPIView(generics.CreateAPIView):
    queryset = PopularReview.objects.all()
    serializer_class = PopularReviewCreateSerializer

    def perform_create(self, serializer):
        # Сначала создаем отзыв
        popular_review_create = serializer.save()

        # Если есть изображения, сохраняем их
        images = self.request.FILES.getlist('images')
        for image in images:
            ReviewImage.objects.create(review=popular_review_create, image=image)

        return popular_review_create

    def post(self, request, *args, **kwargs):
        # Используем CreateAPIView для обработки POST-запроса
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Сначала сохраняем отзыв
            popular_review_create = self.perform_create(serializer)

            # Получаем сериализованные данные для ответа, включая изображения
            response_serializer = PopularReviewSerializer(popular_review_create)

            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ToTryViewSet(viewsets.ModelViewSet):
    queryset = ToTry.objects.all()
    serializer_class = ToTrySerializer


class HotelsListAPIView(generics.ListAPIView):
    serializer_class = HotelsListSerializer

    def get_queryset(self):
        # Аннотируем отели средним рейтингом
        queryset = Hotels.objects.annotate(
            average_rating=Avg('hotel_reviews__rating'),  # Вычисляем средний рейтинг
            is_popular=Case(
                When(average_rating__gte=4, then=Value(1)),  # Если рейтинг >= 4, помечаем как популярный
                default=Value(0),  # В противном случае, помечаем как непопулярный
                output_field=IntegerField(),
            )
        ).order_by('-is_popular', '-average_rating')  # Сортируем сначала по популярности, затем по рейтингу

        return queryset


class HotelsDetailAPIView(generics.RetrieveAPIView):
    queryset = Hotels.objects.all()
    serializer_class = HotelDetailSerializer


class HotelsReviewListAPIView(generics.ListAPIView):
    queryset = HotelsReview.objects.all()
    serializer_class = HotelReviewListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = HotelsReviewFilter


class HotelReviewCreateAPiView(generics.CreateAPIView):
    queryset = HotelsReview.objects.all()
    serializer_class = HotelsReviewCreateSerializer


    def perform_create(self, serializer):
        # Сначала создаем отзыв
        hotel_review_create = serializer.save()

        # Если есть изображения, сохраняем их
        images = self.request.FILES.getlist('images')
        for image in images:
            HotelsReviewImage.objects.create(hotel_review=hotel_review_create, image=image)

        return hotel_review_create

    def post(self, request, *args, **kwargs):
        # Используем CreateAPIView для обработки POST-запроса
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Сначала сохраняем отзыв
            hotel_review_create = self.perform_create(serializer)

            # Получаем сериализованные данные для ответа, включая изображения
            response_serializer = HotelsReviewSerializer(hotel_review_create)

            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# for kitchen

class KitchenListView(generics.ListAPIView):
    serializer_class = KitchenListSerializer

    def get_queryset(self):
        # Аннотируем отели средним рейтингом
        queryset = Kitchen.objects.annotate(
            average_rating=Avg('kitchen_reviews__rating'),  # Вычисляем средний рейтинг
            is_popular=Case(
                When(average_rating__gte=4, then=Value(1)),  # Если рейтинг >= 4, помечаем как популярный
                default=Value(0),  # В противном случае, помечаем как непопулярный
                output_field=IntegerField(),
            )
        ).order_by('-is_popular', '-average_rating')  # Сортируем сначала по популярности, затем по рейтингу

        return queryset


class KitchenDetailView(generics.RetrieveAPIView):
    queryset = Kitchen.objects.all()
    serializer_class = KitchenDetailSerializers


class KitchenReviewCreateAPIView(generics.CreateAPIView):
    queryset = KitchenReview.objects.all()
    serializer_class = KitchenReviewCreateSerializer

    def perform_create(self, serializer):
        # Сначала создаем отзыв
        kitchen_review = serializer.save()

        # Если есть изображения, сохраняем их
        images = self.request.FILES.getlist('images')
        for image in images:
            KitchenReviewImage.objects.create(review=kitchen_review, image=image)

        return kitchen_review

    def post(self, request, *args, **kwargs):
        # Используем CreateAPIView для обработки POST-запроса
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Сначала сохраняем отзыв
            kitchen_review = self.perform_create(serializer)

            # Получаем сериализованные данные для ответа, включая изображения
            response_serializer = KitchenReviewSerializer(kitchen_review)

            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class KitchenReviewListAPIView(generics.ListAPIView):
    queryset = KitchenReview.objects.all()
    serializer_class = KitchenReviewListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = KitchenReviewFilter


class EventListAPiView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializers


class CultureListAPiView(generics.ListAPIView):
    queryset = Culture.objects.all()
    serializer_class = CultureSerializers


class GamesViewSet(viewsets.ModelViewSet):
    queryset = Games.objects.all()
    serializer_class = GamesSerializers


class NationalClothesViewSet(viewsets.ModelViewSet):
    queryset = NationalClothes.objects.all()
    serializer_class = NationalClothesSerializers


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializers


class HandCraftsViewSet(viewsets.ModelViewSet):
    queryset = HandCrafts.objects.all()
    serializer_class = HandCraftsSerializers


class NationalInstrumentsViewSet(viewsets.ModelViewSet):
    queryset = NationalInstruments.objects.all()
    serializer_class = NationalInstrumentsSerializers


class CultureKitchenViewSet(viewsets.ModelViewSet):
    queryset = CultureKitchen.objects.all()
    serializer_class = CultureKitchenSerializers


class GalleryListAPIView(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializers


class GalleryReviewCreateAPIView(generics.CreateAPIView):
    queryset = GalleryReview.objects.all()
    serializer_class = GalleryReviewCreateSerializer

    def perform_create(self, serializer):
        # Сначала создаем отзыв
        gallery_review = serializer.save()

        # Если есть изображения, сохраняем их
        images = self.request.FILES.getlist('images')
        for image in images:
            GalleryReviewImage.objects.create(gallery=gallery_review, image=image)

        return gallery_review

    def post(self, request, *args, **kwargs):
        # Используем CreateAPIView для обработки POST-запроса
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Сначала сохраняем отзыв
            gallery_review = self.perform_create(serializer)

            # Получаем сериализованные данные для ответа, включая изображения
            response_serializer = GalleryReviewSerializer(gallery_review)

            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FavoriteItemViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteSerializers

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        cart, created = Favorite.objects.get_or_create(user=request.user)
        serializer = self.get_serializer(cart)
        return Response(serializer.data)


class FavoriteItemViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteItemSerializers

    def get_queryset(self):
        return FavoriteItem.objects.filter(favorite__user=self.request.user)

    def perform_create(self, serializer):
        cart, created = Favorite.objects.get_or_create(user=self.request.user)
        serializer.save(cart=cart)

