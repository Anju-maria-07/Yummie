from django.contrib import admin
from .models import FoodSpot,Post, PostMedia
# Register your models here.

admin.site.register(FoodSpot)
admin.site.register(Post)
admin.site.register(PostMedia)