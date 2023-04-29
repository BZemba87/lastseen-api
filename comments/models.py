from django.db import models
from django.contrib.auth.models import User
from captions.models import Caption


class Comment(models.Model):
    """
    Comment model for user and caption
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.ForeignKey(Caption, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
