from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Like(models.Model):
    """
    Like model class,
    Credit: Code Institute django rest walkthrough project
    """

    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='likes'
    )
    post = models.ForeignKey(
        Post, related_name='likes', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner.username} likes {self.post.title}'
