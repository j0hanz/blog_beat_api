from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Comment(models.Model):
    """
    Represents a comment made by a user on a specific post.
    Credit: Code Institute django rest walkthrough project
    """

    owner = models.ForeignKey(
        User, related_name='comments', on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE
    )
    content = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
