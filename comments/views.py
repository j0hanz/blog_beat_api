from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions

from blog_beat_api.permissions import IsOwnerOrReadOnly

from .models import Comment
from .serializers import CommentDetailSerializer, CommentSerializer


class CommentList(generics.ListCreateAPIView):
    """View for listing and creating comments.
    Credit: Code Institute django rest walkthrough project.
    """

    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']

    def perform_create(self, serializer) -> None:
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting comments.
    Credit: Code Institute django rest walkthrough project.
    """

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
