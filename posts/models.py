from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Represents a user's post with an image, content, and optional image filter.
    """

    IMAGE_FILTER_CHOICES = [
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

    owner = models.ForeignKey(
        User, related_name='posts', on_delete=models.CASCADE
    )
    title = models.CharField(max_length=150)
    content = models.TextField(blank=False)
    image = models.ImageField(upload_to='images/', blank=True)
    image_filter = models.CharField(
        max_length=32, choices=IMAGE_FILTER_CHOICES, default='normal'
    )
    location = models.CharField(max_length=150, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'


class Favorite(models.Model):
    """
    Represents a user's favorite posts.
    """

    user = models.ForeignKey(
        User, related_name='favorites', on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post, related_name='favorites', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.username} -> {self.post.title}'
