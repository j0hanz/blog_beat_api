from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    country = CountryField(blank=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_nobody_x67hac', blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner.username}'s profile"


class SocialMediaLink(models.Model):
    SOCIAL_MEDIA_CHOICES = [
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('youtube', 'YouTube'),
        ('website', 'Website'),
    ]

    profile = models.ForeignKey(
        Profile, related_name='social_media_links', on_delete=models.CASCADE
    )
    platform = models.CharField(max_length=50, choices=SOCIAL_MEDIA_CHOICES)
    url = models.URLField(max_length=200)

    class Meta:
        unique_together = ('profile', 'platform')

    def __str__(self):
        return f"{self.profile.owner.username} - {self.platform}"
