from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    client = serializers.ReadOnlyField(source='contract.client.username')
    freelancer = serializers.ReadOnlyField(source='contract.freelancer.username')
    project = serializers.ReadOnlyField(source='contract.project.title')

    class Meta:
        model = Review
        fields = ['id', 'contract', 'project', 'client', 'freelancer', 'rating', 'comment', 'created_at']
        read_only_fields = ['id', 'client', 'freelancer', 'project', 'created_at']
