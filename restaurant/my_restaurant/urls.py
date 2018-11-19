from .views import OrdersViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'orders', OrdersViewSet)
urlpatterns = router.urls
