from django.db import models
from django.conf import settings
# Create your models here.

class YumMeetRequest(models.Model):
    STATUS_CHOICES=[
        ('pending','Pending'),
        ('accepted','Accepted'),
        ('declined','Declined'),
        ('cancelled','Cancelled'),
        ('completed','Completed')
    ]


    sender=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='sent_yummeets'
    )
    receiver=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='received_yummeets'
    )
    post=models.ForeignKey(
        'posts.Post',
        on_delete=models.CASCADE,
        related_name='yummeet_requests'
    )
    status=models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-created_at']
        constraints=[
            models.CheckConstraint(
                condition=~models.Q(sender=models.F('receiver')),
                name='prevent_self_yummeet'
            ),
            models.UniqueConstraint(
                fields=['sender','receiver','post'],
                condition=models.Q(status='pending'),
                name='unique_pending_yummeet'
            )
        ]

    def __str__(self):
        return f"{self.sender.username} invited {self.receiver.username}"