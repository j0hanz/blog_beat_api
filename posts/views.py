from rest_framework import generics, permissions
from django.http import Http404
from .models import Post
from .serializers import PostSerializer
from blog_beat_api.permissions import IsOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self):
        try:
            post = super().get_object()
            self.check_object_permissions(self.request, post)
            return post
        except Post.DoesNotExist:
            raise Http404
