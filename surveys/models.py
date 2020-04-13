from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField


class Survey(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    questions = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name}'
