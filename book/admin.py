from django.contrib import admin
from .models import UserProfile, Booking, BookingItem, BookingType
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Booking)
admin.site.register(BookingType)
admin.site.register(BookingItem)