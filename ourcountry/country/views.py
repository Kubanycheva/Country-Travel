from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView
from rest_framework import permissions
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({'detail': 'Неверные учетные данные'}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

# FOR CHARLES DEO


class UserProfileViewSet(viewsets.ModelViewSet):
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


class AttractionReviewViewSet(viewsets.ModelViewSet):
    queryset = AttractionReview.objects.all()
    serializer_class = AttractionReviewSerializer

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


class PopularReviewViewSet(viewsets.ModelViewSet):
    queryset = PopularReview.objects.all()
    serializer_class = PopularReviewSerializer


class ToTryViewSet(viewsets.ModelViewSet):
    queryset = ToTry.objects.all()
    serializer_class = ToTrySerializer


class HotelsListAPIView(generics.ListAPIView):
    queryset = Hotels.objects.all()
    serializer_class = HotelsListSerializer


class HotelsDetailAPIView(generics.RetrieveAPIView):
    queryset = Hotels.objects.all()
    serializer_class = HotelDetailSerializer


class HotelsReviewViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HotelsReview.objects.all()
    serializer_class = HotelsReviewSerializer

    def get_queryset(self):
        return HotelsReview.objects.filter(client_hotel=self.request.user)

# for kitchen


class KitchenListView(generics.ListAPIView):
    queryset = Kitchen.objects.all()
    serializer_class = KitchenListSerializer


class KitchenDetailView(generics.RetrieveAPIView):
    queryset = Kitchen.objects.all()
    serializer_class = KitchenDetailSerializers


class KitchenReviewViewSet(viewsets.ModelViewSet):
    queryset = KitchenReview.objects.all()
    serializer_class = KitchenReviewSerializer


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


class  KitchenReviewAPIView(generics.ListAPIView):
    queryset = KitchenReview.objects.all()
    serializer_class = KitchenReviewSerializer