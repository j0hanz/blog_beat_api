from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin
from .models import Profile, SocialMediaLink
from followers.models import Follower


class SocialMediaLinkSerializer(serializers.ModelSerializer):
    """
    Serializer for the SocialMediaLink model.
    """

    class Meta:
        model = SocialMediaLink
        fields = ['platform', 'url']

    def validate_url(self, value):
        """
        Validate the URL field to ensure it starts with http:// or https://.
        """
        if not value.startswith(('http://', 'https://')):
            raise serializers.ValidationError(
                "URL must start with http:// or https://"
            )
        return value


class ProfileSerializer(CountryFieldMixin, serializers.ModelSerializer):
    """
    Serializer for the Profile model.
    """

    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    social_media_links = SocialMediaLinkSerializer(many=True, required=False)

    def get_is_owner(self, obj):
        """
        Check if the request user is the owner of the profile.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        """
        Get the ID of the following relationship if it exists.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None

    class Meta:
        model = Profile
        fields = [
            'id',
            'owner',
            'first_name',
            'last_name',
            'country',
            'bio',
            'image',
            'created_at',
            'updated_at',
            'is_owner',
            'following_id',
            'posts_count',
            'followers_count',
            'following_count',
            'social_media_links',
        ]
