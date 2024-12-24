from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin


@admin.register(Region, Attractions, Home, PopularPlaces, ToTry, PlacesRegion, Culture,
                Games, NationalClothes, HandCrafts, Currency, NationalInstruments,
                CultureKitchen,
                )
class AllAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(AttractionsImage)
admin.site.register(AttractionReview)


class ReviewImageInline(admin.TabularInline):
    model = ReviewImage
    extra = 1


class PopularReviewAdmin(admin.ModelAdmin):
    inlines = [ReviewImageInline]


admin.site.register(PopularReview, PopularReviewAdmin)


class GalleryReviewInline(admin.TabularInline):
    model = GalleryReview
    extra = 1


@admin.register(Gallery)
class GalleryAdmin(TranslationAdmin):
    inlines = [GalleryReviewInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class HotelsImageInlines(admin.TabularInline):
    model = HotelsImage
    extra = 1


class HotelsReviewInline(admin.TabularInline):
    model = HotelsReview
    extra = 1


@admin.register(Hotels)
class HotelsAdmin(TranslationAdmin):
    inlines = [HotelsReviewInline, HotelsImageInlines]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class KitchenReviewInline(admin.TabularInline):
    model = KitchenReview
    extra = 1


class KitchenLocationInline(admin.TabularInline):
    model = KitchenLocation
    extra = 1


class KitchenImageInline(admin.TabularInline):
    model = KitchenImage
    extra = 1


@admin.register(Kitchen)
class KitchenAdmin(TranslationAdmin):
    inlines = [KitchenReviewInline, KitchenImageInline, KitchenLocationInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class EventInlines(admin.TabularInline):
    model = Event
    extra = 1


class EventCategoriesAdmin(admin.ModelAdmin):
    inlines = [EventInlines]


admin.site.register(EventCategories, EventCategoriesAdmin)
admin.site.register(UserProfile)
admin.site.register(CultureCategory)
admin.site.register(Favorite)
admin.site.register(FavoriteItem)

