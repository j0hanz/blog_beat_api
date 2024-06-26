from django.db import models
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.contrib.auth.models import User


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
        upload_to='images/', default='../default_nobody_x67hac', blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


class SocialMediaLink(models.Model):
    """
    Represents a social media link associated with a user.
    """

    SOCIAL_MEDIA_CHOICES = [
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('youtube', 'YouTube'),
        ('website', 'Website'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.CharField(
        max_length=50, choices=SOCIAL_MEDIA_CHOICES, blank=True
    )
    url = models.URLField(max_length=200, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['owner', 'platform'], name='unique_owner_platform'
            )
        ]

    def __str__(self):
        return f"{self.owner} {self.platform}"


def create_profile(sender, instance, created, **kwargs):
    """
    Function to create a profile once a user is created.
    """
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
