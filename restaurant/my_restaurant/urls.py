from .views import OrdersViewSet
from rest_framework.routers import DefaultRouter
from django.urls import include, path

router = DefaultRouter()
router.register(r"", OrdersViewSet)
urlpatterns = router.urls
urlpatterns.append(path("rest-auth/", include("rest_auth.urls")))
