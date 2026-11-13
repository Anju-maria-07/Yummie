from rest_framework import serializers
from .models import Post,PostMedia

class PostMediaSerializer(serializers.ModelSerializer):

    class Meta:
        model=PostMedia
        fields='__all__'
        read_only=['post','created_at','updated_at']


class PostSerializer(serializers.ModelSerializer):
    
    media= PostMediaSerializer(many=True)

    def create(self,validated_data):
        media_data=validated_data.pop('media',[])
        post=Post.objects.create(**validated_data)

        for media in media_data:
            PostMedia.objects.create(post=post, **media)

        return post

    class Meta:
        model=Post
        fields='__all__'
        read_only=['user','created_at','updated_at']


