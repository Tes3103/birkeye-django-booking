from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Table(models.Model):
    code = models.CharField(max_length=80, null=False,
                            blank=False, unique=True)
    no_of_gusts = models.IntegerField(null=False, blank=False, default=1)

    def _str_(self):
        return self.code


class Booking(models.Model):
    customer_full_name = models.CharField(
        max_length=200, null=False, blank=False)
    customer_email = models.EmailField(max_length=100, null=False, blank=False)
    date = models.DateField(auto_now=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, related_name='booking_spot', blank=False)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date', 'start_time']

    def __str__(self):
        return self.table


class BookingQuery(models.Model):
    """Model for booking query form"""
    date = models.DateField()
