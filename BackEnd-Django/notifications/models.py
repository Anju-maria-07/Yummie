from django.db import models
from django.conf import settings

# Create your models here.
class Notification(models.Model):
    NOTIFICATION_TYPES=[
        ('like','Like'),
        ('comment','Comment'),
        ('follow','Follow'),
        ('yumit','YumIt'),
        ('yummeet','YumMeet')
    ]
    recipient=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notifications'
    )
    actor=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='send_notifications'
    )
    notification_type=models.CharField(
        max_length=20,
        choices=NOTIFICATION_TYPES
    )
    is_read=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    read_at=models.DateTimeField(null=True,blank=True)
    post=models.ForeignKey('posts.Post',
                             on_delete=models.CASCADE,
                             related_name='notifications',
                             null=True,blank=True)

    def __str__(self):
        return f"{self.actor.username}- {self.get_notification_type_display()}"