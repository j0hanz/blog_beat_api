from django.db import models
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class SocialMediaLink(models.Model):
    """
    Represents a social media link associated with a user.
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    SOCIAL_MEDIA_CHOICES = [
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('youtube', 'YouTube'),
        ('website', 'Website'),
    ]
    platform = models.CharField(max_length=50, choices=SOCIAL_MEDIA_CHOICES)
    url = models.URLField(max_length=200)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['owner', 'platform'], name='unique_owner_platform'
            )
        ]
        ordering = ['platform']

    def __str__(self):
        return f"{self.platform} {self.url}"


class Profile(models.Model):
    """
    Represents a user's profile with personal information and an image.
    """

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    country = CountryField(blank=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='images/nobody.webp', blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    """
    Function to create a profile once a user is created.
    """
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
