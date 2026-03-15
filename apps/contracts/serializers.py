from rest_framework import serializers
from .models import Contract

class ContractSerializer(serializers.ModelSerializer):
    client = serializers.ReadOnlyField(source='client.username')
    freelancer = serializers.ReadOnlyField(source='freelancer.username')
    project = serializers.ReadOnlyField(source='project.title')

    class Meta:
        model = Contract
        fields = ['id', 'project', 'client', 'freelancer', 'agreed_price', 'status', 'created_at', 'finished_at']
        read_only_fields = ['id', 'client', 'freelancer', 'project', 'status', 'created_at', 'finished_at']
