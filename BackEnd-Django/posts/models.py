from django.db import models
from django.conf import settings

# Create your models here.
class FoodSpot(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField(blank=True)
    latitude = models.DecimalField(max_digits=9,
                                   decimal_places=6,
                                   blank=True,
                                   null=True)
    longitude = models.DecimalField(max_digits=9,
                                   decimal_places=6,
                                   null=True,blank=True)
    google_place_id = models.CharField(max_length=255,
                                        blank=True,null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,blank=True,
        on_delete = models.SET_NULL,
        related_name = 'suggested_food_spots'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    food_spot=models.ForeignKey(FoodSpot,
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