from django.db import models
from django.contrib.auth.models import User
from captions.models import Caption


class Love(models.Model):
    """
    Love model, related to 'owner' and 'caption'.
    'unique_together' stops user loving same caption more than once.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.ForeignKey(
        Caption, related_name='love', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'caption']

    def __str__(self):
        return f'{self.owner} {self.caption}'
