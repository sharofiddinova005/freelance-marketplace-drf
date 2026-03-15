from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Contract
from .serializers import ContractSerializer
from .permissions import IsClient
from apps.bids.models import Bid
from apps.projects.models import Project
from django.utils import timezone

class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all().order_by('-created_at')
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated]


    @action(detail=False, methods=['post'], url_path='accept-bid/(?P<bid_id>[^/.]+)')
    def accept_bid(self, request, bid_id=None):
        try:
            bid = Bid.objects.get(id=bid_id)
        except Bid.DoesNotExist:
            return Response({"detail": "Bid topilmadi."}, status=status.HTTP_404_NOT_FOUND)

        project = bid.project


        if project.client != request.user:
            return Response({"detail": "Siz bu loyhani boshqara olmaysiz."}, status=status.HTTP_403_FORBIDDEN)


        bid.status = 'accepted'
        bid.save()


        Bid.objects.filter(project=project).exclude(id=bid.id).update(status='rejected')


        project.status = 'in_progress'
        project.save()


        contract = Contract.objects.create(
            project=project,
            client=request.user,
            freelancer=bid.freelancer,
            agreed_price=bid.price
        )

        serializer = self.get_serializer(contract)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    @action(detail=True, methods=['post'], url_path='finish')
    def finish_contract(self, request, pk=None):
        contract = self.get_object()
        project = contract.project


        if contract.client != request.user:
            return Response({"detail": "Siz contractni tugata olmaysiz."}, status=status.HTTP_403_FORBIDDEN)

        contract.status = 'finished'
        contract.finished_at = timezone.now()
        contract.save()

        project.status = 'completed'
        project.save()

        serializer = self.get_serializer(contract)
        return Response(serializer.data)
