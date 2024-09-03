from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django_countries.fields import CountryField


class Profile(models.Model):
    """Represents a user's profile with personal information and an image."""

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    country = CountryField(blank=True)
    bio = models.TextField(blank=True)
    image = CloudinaryField('image', default='nobody_image_wcjcx2', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs) -> None:
    """Function to create a profile once a user is created."""
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
