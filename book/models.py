from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username


class BookingType(models.Model):
    name = models.CharField(max_length=20) 

    def __str__(self):
        return self.name


class BookingItem(models.Model):
    type = models.ForeignKey(BookingType, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    price_per_hour = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Booking(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    item = models.ForeignKey(BookingItem, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} → {self.item}"
