from django.db import models
from django.conf import settings
# Create your models here.

class Follow(models.Model):
    follower=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='following'
    )
    following=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='follower'
    )
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints=[
            models.UniqueConstraint(
                fields=['follower','following'],
                name='unique_user_follow'
            ),
            models.CheckConstraint(
                condition=~models.Q(follower=models.F('following')),
                name='prevent_self_follow'
            )
        ]

    def __str__(self):
        return f"{self.follower.username} follows {self.following.username}"