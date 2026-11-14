from rest_framework import serializers
from .models import Post,PostMedia

class PostMediaSerializer(serializers.ModelSerializer):

    class Meta:
        model=PostMedia
        fields='__all__'
        read_only_fields=['post','created_at','updated_at']


class PostSerializer(serializers.ModelSerializer):
    
    media= PostMediaSerializer(many=True, read_only=True)
    media_files= serializers.ListField(
        child=serializers.FileField()
        write_only=True, required=False
    )

    def create(self,validated_data):
        media_files=validated_data.pop('media_files',[])
        post=Post.objects.create(**validated_data)

        for index,file in enumerate(media_files):
            media_type= 'video' if file.content_type.startswith('video/') else 'image'
            PostMedia.objects.create(post=post,
                                     media_type=media_type,
                                     file=file,
                                     order=index)

        return post

    class Meta:
        model=Post
        fields='__all__'
        read_only_fields=['user','created_at','updated_at']


