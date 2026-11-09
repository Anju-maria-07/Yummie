from django.db import models
from django.conf import settings

# Create your models here.

class Post(models.Model):
    food_spot=models.ForeignKey('foodspots.FoodSpot',
        on_delete=models.PROTECT,
        related_name= 'posts'
    )
    user=models.ForeignKey(settings.AUTH_USER_MODEL,
                           on_delete=models.CASCADE,
                           related_name='posts')
    dish_name=models.CharField(max_length=200)
    description=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.dish_name

class PostMedia(models.Model):
    MEDIA_TYPES= [('image','Image'),
                  ('video','Video')]
    
    post=models.ForeignKey(Post,
                           on_delete=models.CASCADE,
                           related_name='media')
    file=models.FileField(upload_to='posts/')
    media_type=models.CharField(
        max_length=10,
        choices=MEDIA_TYPES
    )
    order=models.PositiveIntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.media_type}-{self.post.dish_name}"

    class Meta:
        constraints=[
            models.UniqueConstraint(
                fields=['post','order'],
                name='unique_media_order_per_post'
            )
        ]

class PostLike(models.Model):
    post=models.ForeignKey(Post,
                           on_delete=models.CASCADE,
                           related_name='likes')
    user=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='post_likes'
    )
    created_at=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        constraints=[
            models.UniqueConstraint(
                fields=['post','user'],
                name='unique_user_post_like'
            )
        ]

    def __str__(self):
        return f"{self.user.username} liked {self.post.dish_name}"

class YumIt(models.Model):
    post=models.ForeignKey(Post,
                           on_delete=models.CASCADE,
                           related_name='yumits')
    user=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='yumits'
    )
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints=[
            models.UniqueConstraint(
            fields=['user','post'],
            name='unique_user_post_yumit'
            )
        ]
    def __str__(self):
        return f"{self.user.username} wanna try {self.post.dish_name}"

class Comment(models.Model):
    post=models.ForeignKey(Post,
                           on_delete=models.CASCADE,
                           related_name='comments')
    user=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    reply_to =models.ForeignKey('self',
                            on_delete=models.CASCADE,
                            null=True, blank=True,
                            related_name='replies')

    def __str__(self):
        return f"{self.user.username} commented on {self.post.dish_name}"


