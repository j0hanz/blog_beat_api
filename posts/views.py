from django.db.models import Count
from rest_framework import generics, permissions, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from blog_beat_api.permissions import IsOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    """
    View for listing and creating posts.
    """

    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comments', distinct=True),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = ['likes__owner__profile', 'owner__profile']
    search_fields = ['owner__username', 'title']
    ordering_fields = ['likes_count', 'comments_count', 'likes__created_at']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, and deleting posts.
    """

    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comments', distinct=True),
    ).order_by('-created_at')


class AddRemoveFavourite(generics.UpdateAPIView):
    """
    View for adding or removing a post from favourites.
    """

    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        user = request.user
        if post.favourites.filter(id=user.id).exists():
            post.favourites.remove(user)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            post.favourites.add(user)
            return Response(status=status.HTTP_201_CREATED)
