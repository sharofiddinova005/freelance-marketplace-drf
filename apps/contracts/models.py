from django.db import models
from apps.users.models import User
from apps.projects.models import Project

class Contract(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('finished', 'Finished'),
        ('cancelled', 'Cancelled'),
    )

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='contracts')
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contracts_as_client')
    freelancer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contracts_as_freelancer')
    agreed_price = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.project.title} - {self.client.username} & {self.freelancer.username}"
