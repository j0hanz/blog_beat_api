import datetime

from rest_framework import serializers

from likes.models import Like
from posts.models import Favorite, Post

MAX_IMAGE_SIZE = 2 * 1024 * 1024  # 2MB in bytes
MAX_IMAGE_DIMENSION = 4096  # pixels


def shortnaturaltime(value) -> str:
    """Convert a datetime value into a short, human-readable format."""
    now = datetime.datetime.now(datetime.UTC)
    delta = now - value

    if delta < datetime.timedelta(minutes=1):
        return 'just now'
    if delta < datetime.timedelta(hours=1):
        return f'{int(delta.total_seconds() // 60)}m'
    if delta < datetime.timedelta(days=1):
        return f'{int(delta.total_seconds() // 3600)}h'
    return f'{delta.days}d'


class PostSerializer(serializers.ModelSerializer):
    """Serializer for the Post model."""

    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    is_favourited = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def validate_image(self, value):
        """Validate the image field to ensure it meets size and dimension constraints."""
        if value.size > MAX_IMAGE_SIZE:
            msg = (
                f'Image size larger than {MAX_IMAGE_SIZE // (1024 * 1024)}MB!'
            )
            raise serializers.ValidationError(msg)
        if value.image.height > MAX_IMAGE_DIMENSION:
            msg = f'Image height larger than {MAX_IMAGE_DIMENSION}px!'
            raise serializers.ValidationError(msg)
        if value.image.width > MAX_IMAGE_DIMENSION:
            msg = f'Image width larger than {MAX_IMAGE_DIMENSION}px!'
            raise serializers.ValidationError(msg)
        return value

    def validate_title(self, value):
        """Validate the title field to ensure it is not empty."""
        if not value.strip():
            msg = 'Title cannot be empty.'
            raise serializers.ValidationError(msg)
        return value

    def validate_content(self, value):
        """Validate the content field to ensure it is not empty."""
        if not value.strip():
            msg = 'Post content cannot be empty.'
            raise serializers.ValidationError(msg)
        return value

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(owner=user, post=obj).first()
            return like.id if like else None
        return None

    def get_is_owner(self, obj):
        """Check if the request user is the owner of the post."""
        request = self.context['request']
        return request.user == obj.owner

    def get_is_favourited(self, obj):
        """Check if the request user has favourited the post."""
        user = self.context['request'].user
        if user.is_authenticated:
            return Favorite.objects.filter(owner=user, post=obj).exists()
        return False

    def get_created_at(self, obj):
        """Return the time since the post was created in a human-readable format."""
        return shortnaturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """Return the time since the post was updated in a human-readable format."""
        return shortnaturaltime(obj.updated_at)

    class Meta:
        model = Post
        fields = [
            'id',
            'owner',
            'is_owner',
            'profile_id',
            'profile_image',
            'title',
            'content',
            'image',
            'image_filter',
            'location',
            'created_at',
            'updated_at',
            'like_id',
            'likes_count',
            'comments_count',
            'is_favourited',
        ]


class FavoriteSerializer(serializers.ModelSerializer):
    """Serializer for the Favorite model."""

    class Meta:
        model = Favorite
        fields = ['id', 'owner', 'post', 'created_at']
