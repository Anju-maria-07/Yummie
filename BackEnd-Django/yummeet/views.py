from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import YumMeetRequest
# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def accept_yummeet(request,pk):
    try:
        yummeet_request=YumMeetRequest.objects.get(pk=pk)

        if yummeet_request.receiver != request.user:
            return Response(
                {'error':'You are not allowed to accept the invitation.'},
                status=status.HTTP_403_FORBIDDEN
            )

        if yummeet_request.status != 'pending':
            return Response(
                {'error':'Invitation is no longer pending.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if yummeet_request.expires_at < timezone.now():
            yummeet_request.status= 'expired'
            yummeet_request.save(update_fields=['status','updated_at'])
            return Response(
                {'error':'This Invitation is already expired'},
                status=status.HTTP_400_BAD_REQUEST
            )
            
    except YumMeetRequest.DoesNotExist:
        return Response(
            {'error':'YumMeet request not found.'},
            status=status.HTTP_404_NOT_FOUND
        )

    yummeet_request.status='accepted'
    yummeet_request.save()

    return Response(
        {'message':'YumMeet invitation accepted successfullly.'},
        status=status.HTTP_200_OK
    )