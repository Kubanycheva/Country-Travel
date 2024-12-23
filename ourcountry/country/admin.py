from django.contrib import admin
from .models import *


# FOR CHARLES DEO

# FOR HOME


class AttractionReviewInline(admin.TabularInline):
    model = AttractionReview
    extra = 1


class AttractionsImageInline(admin.TabularInline):
    model = AttractionsImage
    extra = 1


class AttractionsAdmin(admin.ModelAdmin):
    inlines = [AttractionReviewInline, AttractionsImageInline]


admin.site.register(Home)
admin.site.register(Attractions, AttractionsAdmin)

# FOR REGIONS

admin.site.register(Region)


class ReviewImageInline(admin.TabularInline):
    model = ReviewImage
    extra = 1


class PopularReviewAdmin(admin.ModelAdmin):
    inlines = [ReviewImageInline]


admin.site.register(PopularReview, PopularReviewAdmin)
admin.site.register(PopularPlaces)


admin.site.register(ToTry)

# FOR GALLERY


class GalleryReviewInline(admin.TabularInline):
    model = GalleryReview
    extra = 1


class GalleryAdmin(admin.ModelAdmin):
    inlines = [GalleryReviewInline]


admin.site.register(Gallery, GalleryAdmin)


# FOR CULTURE
admin.site.register(Culture)
admin.site.register(Games)
admin.site.register(NationalClothes)
admin.site.register(HandCrafts)
admin.site.register(Currency)
admin.site.register(NationalInstruments)


# FOR FIVE_CATEGORIES

admin.site.register(PlacesRegion)


class HotelsImageInlines(admin.TabularInline):
    model = HotelsImage
    extra = 1


class HotelsReviewInline(admin.TabularInline):
    model = HotelsReview
    extra = 1


class HotelsAdmin(admin.ModelAdmin):
    inlines = [HotelsReviewInline, HotelsImageInlines]


admin.site.register(Hotels, HotelsAdmin)

# FOR Hotels
# for kitchen


class KitchenReviewInline(admin.TabularInline):
    model = KitchenReview
    extra = 1


class KitchenLocationInline(admin.TabularInline):
    model = KitchenLocation
    extra = 1


class KitchenImageInline(admin.TabularInline):
    model = KitchenImage
    extra = 1


class KitchenAdmin(admin.ModelAdmin):
    inlines = [KitchenReviewInline, KitchenImageInline, KitchenLocationInline]


admin.site.register(Kitchen, KitchenAdmin)
admin.site.register(Favorite)
admin.site.register(FavoriteItem)


class EventInlines(admin.TabularInline):
    model = Event
    extra = 1


class EventCategoriesAdmin(admin.ModelAdmin):
    inlines = [EventInlines]


admin.site.register(EventCategories, EventCategoriesAdmin)
admin.site.register(CultureCategory)
