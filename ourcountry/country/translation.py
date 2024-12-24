from .models import (Region, Home, Attractions, PopularPlaces, ToTry,  PlacesRegion, Hotels, Kitchen,
                     Gallery, Culture, Games, NationalClothes, HandCrafts, Currency, NationalInstruments,
                     CultureKitchen,)
from modeltranslation.translator import TranslationOptions, register


@register(Region)
class RegionTranslationOptions(TranslationOptions):
    fields = ('region_name', 'region_description')


@register(Home)
class HomeTranslationOptions(TranslationOptions):
    fields = ('home_name', 'home_description')


@register(Attractions)
class AttractionsTranslationOptions(TranslationOptions):
    fields = ('attraction_name', 'description')


@register(PopularPlaces)
class PopularPlacesTranslationOptions(TranslationOptions):
    fields = ('popular_name', 'description')


@register(ToTry)
class ToTryTranslationOptions(TranslationOptions):
    fields = ('to_name', 'description', 'first_description', 'second_description')


@register(PlacesRegion)
class PlacesRegionTranslationOptions(TranslationOptions):
    fields = ('user_name', 'text')


@register(Hotels)
class HotelsTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'address', 'cars_bikes')


@register(Kitchen)
class KitchenTranslationOptions(TranslationOptions):
    fields = ('kitchen_name', 'description')


@register(Gallery)
class GalleryTranslationOptions(TranslationOptions):
    fields = ('gallery_name', )


@register(Culture)
class CultureTranslationOptions(TranslationOptions):
    fields = ('culture_name', 'culture_description')


@register(Games)
class GamesTranslationOptions(TranslationOptions):
    fields = ('games_name', 'games_description')


@register(NationalClothes)
class NationalClothesTranslationOptions(TranslationOptions):
    fields = ('clothes_name', 'clothes_description')


@register(HandCrafts)
class HandCraftsTranslationOptions(TranslationOptions):
    fields = ('hand_name', 'hand_description')


@register(Currency)
class CurrencyTranslationOptions(TranslationOptions):
    fields = ('currency_name', 'currency_description')


@register(NationalInstruments)
class CultureTranslationOptions(TranslationOptions):
    fields = ('national_name', 'national_description')


@register(CultureKitchen)
class CultureTranslationOptions(TranslationOptions):
    fields = ('kitchen_name', 'kitchen_description')
