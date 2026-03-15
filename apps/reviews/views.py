from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Review
from .serializers import ReviewSerializer
from .permissions import IsProjectClient

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by('-created_at')
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'], url_path='freelancer/(?P<freelancer_id>[^/.]+)')
    def freelancer_reviews(self, request, freelancer_id=None):
        reviews = Review.objects.filter(contract__freelancer_id=freelancer_id)
        serializer = self.get_serializer(reviews, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        queryset = Review.objects.all().order_by('-created_at')
        freelancer_id = self.kwargs.get('freelancer_id')
        if freelancer_id is not None:
            return queryset.filter(contract__freelancer_id=freelancer_id)

        return queryset

    def get_permissions(self):
        if self.action in ['create']:
            self.permission_classes = [IsAuthenticated, IsProjectClient]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def perform_create(self, serializer):
        contract_id = self.request.data.get('contract')
        serializer.save(contract_id=contract_id)
