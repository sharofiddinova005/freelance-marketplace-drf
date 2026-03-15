from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    client = serializers.ReadOnlyField(source='client.username')

    class Meta:
        model = Project
        fields = ['id', 'client', 'title', 'description', 'budget', 'deadline', 'status', 'created_at']
        read_only_fields = ['id', 'client', 'status', 'created_at']
