from django.urls import path
from . import views

urlpatterns = [
    path("options/", views.options),
    path("admin/bookings/", views.admin_bookings),
    path("admin/bookings/<int:booking_id>/approve/", views.approve_booking),
    path("admin/bookings/<int:booking_id>/decline/", views.decline_booking),
    path("admin/bookings/<int:booking_id>/delete/", views.delete_booking),
    path("bookings/", views.get_bookings),
    path("bookings/my/", views.user_bookings),
    path("bookings/my/<int:booking_id>/", views.user_booking),
    path("book/", views.book)
]