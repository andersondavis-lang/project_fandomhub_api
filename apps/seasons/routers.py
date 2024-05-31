"""Routers for Seasons App."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets import SeasonViewSet


router_v1 = DefaultRouter()
router_v1.register(r"seasons", SeasonViewSet, basename="season")

urlpatterns = [path("api/v1/", include(router_v1.urls))]
