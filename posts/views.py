from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.http import Http404
from .models import Post
from .serializers import PostSerializer
from blog_beat_api.permissions import IsOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
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
        'likes__created_at',
    ]
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True),
    ).order_by('-created_at')

    def get_object(self):
        try:
            post = super().get_object()
            self.check_object_permissions(self.request, post)
            return post
        except Post.DoesNotExist:
            raise Http404
