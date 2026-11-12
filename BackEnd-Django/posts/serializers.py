from rest_framework import serializers
from .models import Post,PostMedia

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model=Post
        fields='__all__'
        read_only=['user','created_at','updated_at']


class PostMediaSerializer(serializers.ModelSerializer):

    class Meta:
        model=PostMedia,
        fields='__all__'
        read_only=['post','created_at','updated_at']
