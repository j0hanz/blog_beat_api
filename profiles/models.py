from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    country = CountryField(blank=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_nobody_x67hac'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner.username}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)