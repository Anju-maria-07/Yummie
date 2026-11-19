from rest_framework import serializers
from .models import FoodSpot

class FoodSpotSerializer(serializers.ModelSerializer):

    class Meta:
        model=FoodSpot
        fields=['id','name','address','latitude','longitude']