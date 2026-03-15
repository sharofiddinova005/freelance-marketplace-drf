from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet

router = DefaultRouter()
router.register(r'', ReviewViewSet, basename='reviews')

urlpatterns = [
    path('freelancer/<int:freelancer_id>/', ReviewViewSet.as_view({'get': 'list'}), name='freelancer-reviews'),
    path('', include(router.urls)),
]

