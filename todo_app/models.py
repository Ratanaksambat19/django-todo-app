from django.db import models
from django.utils import timezone
# Create your models here.


class Task(models.Model):
    """Daily task database went here"""

    title = models.CharField(max_length = 200)
    complete = models.BooleanField(default = False)
    created = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
