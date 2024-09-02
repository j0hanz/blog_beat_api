from rest_framework import generics, permissions

from blog_beat_api.permissions import IsOwnerOrReadOnly

from .models import Follower
from .serializers import FollowerSerializer


class FollowerList(generics.ListCreateAPIView):
    """View for listing and creating followers.
    Credit: Code Institute django rest walkthrough project.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    def perform_create(self, serializer) -> None:
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """View for retrieving and deleting followers.
    Credit: Code Institute django rest walkthrough project.
    """

    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
