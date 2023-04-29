from django.db import models
from django.contrib.auth.models import User
from caption.models import Caption
# Create your models here.

class Fave(models.model):
    """
    Fave model is related to Owner and Caption model
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.ForeignKey(Caption, related_name='fave',
                                on_delete=models.CASCADE
                                )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        unique_together = ['owner', 'caption']

    def __str__(self):
        return f'{self.owner} {self.caption}'

