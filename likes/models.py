from django.contrib.auth.models import User
from django.db import models

from posts.models import Post


class Like(models.Model):
    """Represents a like on a post by a user.
    Credit: Code Institute django rest walkthrough project.
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post,
        related_name='likes',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(
                fields=['owner', 'post'],
                name='unique_like',
            ),
        ]

    def __str__(self) -> str:
        return f'{self.owner} likes {self.post}'
