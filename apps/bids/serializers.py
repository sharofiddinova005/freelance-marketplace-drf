from rest_framework import serializers
from .models import Bid

class BidSerializer(serializers.ModelSerializer):
    freelancer = serializers.ReadOnlyField(source='freelancer.username')

    class Meta:
        model = Bid
        fields = ['id', 'project', 'freelancer', 'price', 'message', 'status', 'created_at']
        read_only_fields = ['id', 'freelancer', 'status', 'created_at']
