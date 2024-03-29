from rest_framework import routers
from .views import ImageViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'iam', ImageViewSet)

urlpatterns = [
    path('',include(router.urls))
]