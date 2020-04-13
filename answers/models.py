from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User
from surveys.models import Survey


class Answer(models.Model):
    survey_id = models.ForeignKey(Survey, on_delete=models.DO_NOTHING, null=False)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False)
    answers = JSONField()
    answered = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.survey_id, self.user_id, self.answered}'
