from book.models import UserProfile, Booking, BookingItem, BookingType
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'username, phone_number']


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingType
        fields = ["id", "name"]
    
class ItemSerializer(serializers.ModelSerializer):
    type = TypeSerializer(read_only=True)
    type_id = serializers.PrimaryKeyRelatedField(
        queryset=BookingType.objects.all(),
        source="type",
        write_only=True
    )

    class Meta:
        model = BookingItem
        fields = ["id", "name", "price_per_hour", "type", "type_id"]

class BookingSerializer(serializers.ModelSerializer):
    user = ProfileSerializer(read_only=True)
    item = ItemSerializer(read_only=True)

    item_id = serializers.PrimaryKeyRelatedField(
        queryset=BookingItem.objects.all(),
        source="item",
        write_only=True
    )

    class Meta:
        model = Booking
        fields = [ "id", "user", "item", "item_id", "start_time", "end_time", "is_approved"]
        read_only_fields = ["is_approved"]
    
    def create(self, validated_data):
        request = self.context["request"]
        validated_data["user"] = request.user.userprofile
        return super().create(validated_data)

    def validate(self, data):
        if data["start_time"] >= data["end_time"]:
            raise serializers.ValidationError("End time must be after start time")
        return data 



