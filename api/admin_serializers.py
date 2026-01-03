from book.models import UserProfile, Booking, BookingItem
from rest_framework import serializers
from user_serializers import ProfileSerializer, ItemSerializer

class AdminBookingSerializers(serializers.ModelSerializer):
    user = ProfileSerializer(read_only=True)
    item = ItemSerializer(read_only=True)

    user_id = serializers.PrimaryKeyRelatedField(
        queryset=UserProfile.objects.all(),
        source="user",
        write_only=True,
        required=False
    )

    item_id = serializers.PrimaryKeyRelatedField(
        queryset=BookingItem.objects.all(),
        source="item",
        write_only=True,
        required=False
    )
    
    class Meta:
        model = Booking
        fields= ["id", "user", "user_id", "item", "item_id", "start_time", "end_time", "is_approved"]
    

