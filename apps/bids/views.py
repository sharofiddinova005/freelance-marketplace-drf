from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Bid
from .serializers import BidSerializer
from .permissions import IsFreelancer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status as drf_status
from apps.projects.models import Project

class BidViewSet(viewsets.ModelViewSet):
    queryset = Bid.objects.all().order_by('-created_at')
    serializer_class = BidSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated, IsFreelancer]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(freelancer=self.request.user)


    @action(detail=False, methods=['get'], url_path='project/(?P<project_id>[^/.]+)')
    def project_bids(self, request, project_id=None):
        project = Project.objects.get(id=project_id)
        if project.client != request.user:
            return Response({"detail": "Siz bu project bidlarini ko‘ra olmaysiz."}, status=drf_status.HTTP_403_FORBIDDEN)
        bids = Bid.objects.filter(project=project)
        serializer = self.get_serializer(bids, many=True)
        return Response(serializer.data)

