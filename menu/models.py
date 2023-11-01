from django.db import models
from cloudinary.models import CloudinaryField
from django.conf import settings


class Meal(models.Model):
    name = models.CharField(max_length=150, unique=True)
    cover = CloudinaryField('image')
    price = models.IntegerField()

    def _str_(self):
        return self.name


class Favourite(models.Model):
    user = models.ForeignKey(Meal, on_delete=models.CASCADE,
                             related_name='choosen_food', blank=True)
    meal = models.ForeignKey(
        Meal, on_delete=models.CASCADE, related_name='favourite', blank=True)

    class Meta:
        ordering = ['meal']

    def _str_(self):
        return self.user
