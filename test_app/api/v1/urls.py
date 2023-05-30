
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ModelAViewSet
router = DefaultRouter()
router.register('modela', ModelAViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
