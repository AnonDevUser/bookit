from rest_framework.decorators import api_view, permission_classes#, permission_classes
from .user_serializers import ProfileSerializer, BookingSerializer, ItemSerializer, TypeSerializer
from .admin_serializers import AdminBookingSerializers
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def options(request):
    return Response ({ 
        "message": "works"

    }, status=200)

@api_view(["GET"])
@permission_classes([IsAdminUser])
def admin_bookings(request):
    return Response ({ 
        "message": "works"

    }, status=200)

@api_view(["PATCH"])
@permission_classes([IsAdminUser])
def approve_booking(request, booking_id):
    return Response ({ 
        "message": "works"

    }, status=200)

@api_view(["PATCH"])
@permission_classes([IsAdminUser])
def decline_booking(request, booking_id):
    return Response ({ 
        "message": "works"

    }, status=200)

@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def delete_booking(request, booking_id):
    return Response ({ 
        "message": "works"

    }, status=200)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_bookings(request):
    return Response ({ 
        "message": "works"

    }, status=200)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_bookings(request):
    return Response ({ 
        "message": "works"

    }, status=200)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_booking(request, booking_id):
    return Response ({ 
        "message": "works"

    }, status=200)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def book(request):
    return Response ({ 
        "message": "works"

    }, status=200)