
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .api.category import CategoryView
from .api.location import LocationView
from .api.provider import ProviderView

router = DefaultRouter()

router.register("category", CategoryView)
router.register("location", LocationView)
router.register("provider", ProviderView)


urlpatterns = [path("", include("rest_framework.urls")),path("api/", include(router.urls)),]