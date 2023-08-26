from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Content(models.Model):
    """A Model for contents information including content's title, context
    amount of users that rated and average rate"""

    title = models.CharField(blank=True, null=True, max_length=100)

    context = models.TextField(blank=True, null=True)

    user_count = models.IntegerField(default=0)

    rate_mean = models.FloatField(default=0)


class Rate(models.Model):
    """A Model including information about rating contents
    such as user and rate number between 0 and 5"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    content = models.ForeignKey(Content, on_delete=models.CASCADE)

    rate = models.PositiveIntegerField(default=0, validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ])

    class Meta:
        indexes = [
            models.Index(fields=['user', 'content']),
        ]
