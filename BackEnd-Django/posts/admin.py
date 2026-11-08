from django.contrib import admin
from .models import FoodSpot,Post, PostMedia, PostLike,YumIt,Comment
# Register your models here.

admin.site.register(FoodSpot)
admin.site.register(Post)
admin.site.register(PostMedia)
admin.site.register(PostLike)
admin.site.register(YumIt)
admin.site.register(Comment)