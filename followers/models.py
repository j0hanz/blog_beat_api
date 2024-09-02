from django.contrib.auth.models import User
from django.db import models


class Follower(models.Model):
    """Represents a user following another user.
    Credit: Code Institute django rest walkthrough project.
    """

    owner = models.ForeignKey(
        User,
        related_name='following',
        on_delete=models.CASCADE,
    )
    followed = models.ForeignKey(
        User,
        related_name='followed',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(
                fields=['owner', 'followed'],
                name='unique_follow',
            ),
        ]

    def __str__(self) -> str:
        return f'{self.owner} follows {self.followed}'
