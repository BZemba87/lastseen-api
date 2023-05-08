from django.db import models
from django.contrib.auth.models import User


class Caption(models.Model):
    """
    Caption model for owner
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    location = models.CharField(blank=True, null=True, max_length=255)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_qdjgyp', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
