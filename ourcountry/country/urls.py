from django.urls import path, include
from .views import *
from rest_framework import routers


# FOR CHARLES DEO
router = routers.DefaultRouter()
router.register(r'user', UserProfileViewSet, basename='user-list')

urlpatterns = [
    path('', include(router.urls))
]
