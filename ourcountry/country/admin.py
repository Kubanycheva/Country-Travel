from django.contrib import admin
from .models import *


# FOR CHARLES DEO
admin.site.register(UserProfile)

# FOR HOME

class HomeReviewInline(admin.TabularInline):
    model = HomeReview
    extra = 1


class AttractionsHomeAdmin(admin.ModelAdmin):
    inlines = [HomeReviewInline]


admin.site.register(Home)
admin.site.register(AttractionsHome, AttractionsHomeAdmin)
admin.site.register(AttractionCulture)

# FOR REGIONS


class PopularReviewInline(admin.TabularInline):
    model = PopularReview
    extra = 1


class PopularRegionAdmin(admin.ModelAdmin):
    inlines = [PopularReviewInline]


admin.site.register(Region)
admin.site.register(PopularRegion, PopularRegionAdmin)
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

# FOR Hotels


class HotelsReviewInline(admin.TabularInline):
    model = HotelsReview
    extra = 1


class HotelsRegionAdmin(admin.ModelAdmin):
    inlines = [HotelsReviewInline]


admin.site.register(HotelsRegion, HotelsRegionAdmin)
admin.site.register(HotelsReview)

# FOR Hotels


class HotelsReviewInline(admin.TabularInline):
    model = HotelsReview
    extra = 1


class HotelsRegionAdmin(admin.ModelAdmin):
    inlines = [HotelsReviewInline]

# for kitchen


class KitchenReviewInline(admin.TabularInline):
    model = KitchenReview
    extra = 1


class KitchenAdmin(admin.ModelAdmin):
    inlines = [KitchenReviewInline]


admin.site.register(Kitchen, KitchenAdmin)


# FOR event

#  7 categories

admin.site.register(Concert)
admin.site.register(EventConcert)
admin.site.register(Cinema)
admin.site.register(EventCinema)
admin.site.register(Leisure)
admin.site.register(EventLeisure)
admin.site.register(Theater)
admin.site.register(EventTheater)
admin.site.register(MasterClasses)
admin.site.register(EventMaster)
admin.site.register(Tourism)
admin.site.register(EventTourism)


#FOR Attractions

admin.site.register(AttractionsEvent)
admin.site.register(AttractionsEventReview)

# FOR FAVORITE


admin.site.register(Favorite)
admin.site.register(FavoriteItem)

