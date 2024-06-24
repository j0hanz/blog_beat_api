from rest_framework import serializers
from posts.models import Post
from likes.models import Like


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the Post model.
    """

    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    is_favourited = serializers.SerializerMethodField()

    def validate_image(self, value):
        """
        Validate the image field to ensure it meets size and dimension constraints.
        """
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def validate_title(self, value):
        """
        Validate the title field to ensure it is not empty.
        """
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_content(self, value):
        """
        Validate the content field to ensure it is not empty.
        """
        if not value.strip():
            raise serializers.ValidationError("Post content cannot be empty.")
        return value

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(owner=user, post=obj).first()
            return like.id if like else None
        return None

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_is_favourited(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return obj.favourites.filter(id=user.id).exists()
        return False

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
