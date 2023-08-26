from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Content(models.Model):
    title = models.CharField(blank=True, Null=True, max_length=100)

    context = models.TextField(blank=True, null=True)

    user_count = models.IntegerField(default=0)

    rate_mean = models.FloatField(default=0)


class Rate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    content = models.ForeignKey(Content, on_delete=models.CASCADE)

    rate = models.IntegerField(default=0, validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
    # @property
    # def average_rating(self):
    #     return self.rate_mean.aggregate(Avg('rating'))['rating_avg']