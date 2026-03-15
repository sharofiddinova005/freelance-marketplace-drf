from rest_framework.routers import DefaultRouter
from .views import BidViewSet

router = DefaultRouter()
router.register(r'', BidViewSet, basename='bids')

urlpatterns = router.urls
