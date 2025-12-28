from rest_framework.decorators import api_view #, permission_classes
from .serializers import ProfileSerializer, BookingSerializer, ItemSerializer, TypeSerializer
#from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(["GET"])
def options(request):
    return Response ({ 
        "message": "works"

    }, status=200)

@api_view(["GET"])
def admin_bookings(request):
    return Response ({ 
        "message": "works"

    }, status=200)

@api_view(["PATCH"])
def approve_booking(request, booking_id):
    return Response ({ 
        "message": "works"

    }, status=200)

@api_view(["PATCH"])
def decline_booking(request, booking_id):
    return Response ({ 
        "message": "works"

    }, status=200)

@api_view(["DELETE"])
def delete_booking(request, booking_id):
    return Response ({ 
        "message": "works"

    }, status=200)

@api_view(["GET"])
def get_bookings(request):
    return Response ({ 
        "message": "works"

    }, status=200)

@api_view(["GET"])
def user_bookings(request):
    return Response ({ 
        "message": "works"

    }, status=200)

@api_view(["GET"])
def user_booking(request, booking_id):
    return Response ({ 
        "message": "works"

    }, status=200)

@api_view(["POST"])
def book(request):
    return Response ({ 
        "message": "works"

    }, status=200)