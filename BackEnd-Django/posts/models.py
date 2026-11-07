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

class PostMedia(models.Model):
    MEDIA_TYPES= [('image','Image'),
                  ('video','Video')]
    
    post=models.FOreignKey(Post,
                           on_delete=models.CASCADE,
                           related_name='media')
    file=models.FileField(upload_to='posts/')
    media_types=models.CharField(
        max_length=10
        choices=MEDIA_TYPES
    )