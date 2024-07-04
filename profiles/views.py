from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count
from .models import Profile, SocialMediaLink
from .serializers import ProfileSerializer, SocialMediaLinkSerializer
from blog_beat_api.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    """
    View for listing profiles.
    """

    queryset = Profile.objects.annotate(
        posts_count=Count('owner__posts', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = [
        'owner__following__followed__profile',
        'owner__followed__owner__profile',
    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followers__created_at',
    ]


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, and deleting profiles.
    """

    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__posts', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer


class SocialMediaLinkList(generics.ListCreateAPIView):
    """
    View for listing and creating social media links.
    """

    queryset = SocialMediaLink.objects.all()
    serializer_class = SocialMediaLinkSerializer


class SocialMediaLinkDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, and deleting social media links.
    """

    queryset = SocialMediaLink.objects.all()
    serializer_class = SocialMediaLinkSerializer
    permission_classes = [IsOwnerOrReadOnly]
