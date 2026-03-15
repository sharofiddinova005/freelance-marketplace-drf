from django.db import models
from apps.contracts.models import Contract

class Review(models.Model):
    RATING_CHOICES = [(i, i) for i in range(1, 6)]

    contract = models.OneToOneField(Contract, on_delete=models.CASCADE, related_name='review')
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.contract.project.title} by {self.contract.client.username}"
