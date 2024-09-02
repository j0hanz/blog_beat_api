from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, permissions, status
from rest_framework.response import Response

from blog_beat_api.permissions import IsOwnerOrReadOnly

from .models import Favorite, Post
from .serializers import FavoriteSerializer, PostSerializer


class PostList(generics.ListCreateAPIView):
    """View for listing and creating posts."""

    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comments', distinct=True),
        favorites_count=Count('favorites', distinct=True),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'favorites__owner__profile',
        'owner__profile',
    ]
    search_fields = ['owner__username', 'title']
    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at',
        'favorites__created_at',
    ]

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if 'favorites' in self.request.query_params and user.is_authenticated:
            queryset = queryset.filter(favorites__owner=user)
        return queryset

    def perform_create(self, serializer) -> None:
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting posts."""

    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comments', distinct=True),
        favorites_count=Count('favorites', distinct=True),
    ).order_by('-created_at')


class FavoritePost(generics.GenericAPIView):
    """View for adding or removing a post from favorites."""

    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs['pk'])
        user = request.user
        favorite, created = Favorite.objects.get_or_create(
            owner=user,
            post=post,
        )
        if created:
            return Response(
                {'status': 'added to favorites'},
                status=status.HTTP_201_CREATED,
            )
        favorite.delete()
        return Response(
            {'status': 'removed from favorites'},
            status=status.HTTP_204_NO_CONTENT,
        )

    def delete(self, request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs['pk'])
        user = request.user
        favorite = Favorite.objects.filter(owner=user, post=post).first()
        if favorite:
            favorite.delete()
            return Response(
                {'status': 'removed from favorites'},
                status=status.HTTP_204_NO_CONTENT,
            )
        return Response(
            {'status': 'not in favorites'},
            status=status.HTTP_400_BAD_REQUEST,
        )
