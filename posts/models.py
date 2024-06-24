from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Represents a user's post with an image, content, and optional image filter.
    """

    image_filter_choices = [
        ('_1977', '1977'),
        ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'),
        ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'),
        ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'),
        ('normal', 'Normal'),
        ('nashville', 'Nashville'),
        ('rise', 'Rise'),
        ('toaster', 'Toaster'),
        ('valencia', 'Valencia'),
        ('walden', 'Walden'),
        ('xpro2', 'X-pro II'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_nobody_x67hac', blank=True
    )
    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal'
    )
    location = models.CharField(max_length=150, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Meta class for Post model.
        """

        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'


class Bookmark(models.Model):
    """
    Represents a bookmark created by a user for a specific post.
    """

    owner = models.ForeignKey(
        User, related_name='bookmarks', on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post, related_name='bookmarks', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Meta class for Bookmark model.
        """

        unique_together = ('owner', 'post')

    def __str__(self):
        return f'{self.owner.username} bookmarked {self.post.title}'
