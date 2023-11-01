from django.db import models
from django.contrib.auth.models import User
import datetime


class Review(models.Model):
    title = models.CharField(max_length=80, unique=True, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='feedback')
    date_created_on = models.DateTimeField(auto_now=True)
    date_updated_on = models.DateTimeField(auto_now=True)
    rate = models.PositiveSmallIntegerField()
    review_text = models.TextField()

    class Meta:
        ordering = ['-date_updated_on']

    def _str_(self):
        return f"Review {self.review_text} by {self.author}"
