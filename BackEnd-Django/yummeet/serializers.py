from rest_framework import serializers
from .models import YumMeetRequest
from posts.models import YumIt
from connections.models import Follow

class YumMeetRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model=YumMeetRequest
        fields='__all__'
        read_only_fields=['sender','status',
                          'created_at','updated_at']

    def validate(self,attrs):
        sender= self.context['request'].user
        receiver= attrs['receiver']
        post =attrs['post']

        if sender==receiver:
            raise serializers.ValidationError(
                'you cant invite yourself !'
                )

        sender_yumited=YumIt.objects.filter(
            user=sender,
            post=post
            ).exists()
        receiver_yumited=YumIt.objects.filter(
            user=receiver,
            post=post
            ).exists()

        if not sender_yumited or not receiver_yumited :
                raise serializers.ValidationError(
                    'Both users must YumIt the same post.'
                )

        sender_follows_receiver=Follow.objects.filter(
             follower=sender,
             following=receiver
        ).exists()
        receiver_follows_sender=Follow.objects.filter(
             follower=receiver,
             following=sender
        ).exists()

        if not sender_follows_receiver or not receiver_follows_sender:
             raise serializers.ValidationError(
                  'both userd should follow each other'
             )
             
        return attrs