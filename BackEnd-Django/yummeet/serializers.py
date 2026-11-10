from rest_framework import serializers
from .models import YumMeetRequest

class YumMeetRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model=YumMeetRequest
        fields='__all__'