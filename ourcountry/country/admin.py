from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(Home)
admin.site.register(Regions)
admin.site.register(CountryFood)
admin.site.register(PopularPlaces)
admin.site.register(PopularReview)