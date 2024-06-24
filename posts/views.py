from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.http import Http404
from .models import Post, Bookmark
from .serializers import PostSerializer, BookmarkSerializer
from blog_beat_api.permissions import IsOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    """
    View for listing and creating posts.
    """

    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comments', distinct=True),
        bookmarks_count=Count('bookmarks', distinct=True),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'likes__owner__profile',
        'owner__profile',
    ]
    search_fields = [
        'owner__username',
        'title',
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'bookmarks_count',
        'likes__created_at',
    ]
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

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
        bookmarks_count=Count('bookmarks', distinct=True),
    ).order_by('-created_at')

    def get_object(self):
        """
        Retrieve the post object, raising 404 if not found.
        """
        try:
            post = super().get_object()
            self.check_object_permissions(self.request, post)
            return post
        except Post.DoesNotExist:
            raise Http404


class BookmarkList(generics.ListCreateAPIView):
    """
    View for listing and creating bookmarks.
    """

    serializer_class = BookmarkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Return bookmarks for the request user.
        """
        return Bookmark.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookmarkDetail(generics.RetrieveDestroyAPIView):
    """
    View for retrieving and deleting bookmarks.
    """

    serializer_class = BookmarkSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)
