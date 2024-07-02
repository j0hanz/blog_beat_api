from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin
from .models import Profile, SocialMediaLink
from followers.models import Follower


class SocialMediaLinkSerializer(serializers.ModelSerializer):
    """
    Serializer for the SocialMediaLink model.
    This serializer validates URLs to ensure they start with "http://" or "https://".
    """

    def validate_url(self, value):
        """
        Validate the URL field to ensure it starts with http:// or https://.
        """
        if not value.startswith(('http://', 'https://')):
            raise serializers.ValidationError(
                "URL must start with http:// or https://"
            )
        return value

    class Meta:
        model = SocialMediaLink
        fields = ['id', 'platform', 'url']


class ProfileSerializer(CountryFieldMixin, serializers.ModelSerializer):
    """
    Serializer for the Profile model.
    This serializer handles creating and updating of profiles along with their nested social media links.
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

    def create(self, validated_data):
        """
        Custom create method to handle nested social media links.
        """
        social_media_links_data = validated_data.pop('social_media_links', [])
        profile = Profile.objects.create(**validated_data)
        for link_data in social_media_links_data:
            SocialMediaLink.objects.create(owner=profile.owner, **link_data)
        return profile

    def update(self, instance, validated_data):
        """
        Custom update method to handle nested social media links.
        Updates profile fields and processes updates or creation of social media links.
        """
        social_media_links_data = validated_data.pop('social_media_links', [])

        instance.first_name = validated_data.get(
            'first_name', instance.first_name
        )
        instance.last_name = validated_data.get(
            'last_name', instance.last_name
        )
        instance.country = validated_data.get('country', instance.country)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.image = validated_data.get('image', instance.image)
        instance.save()

        for link_data in social_media_links_data:
            link_id = link_data.get('id', None)
            if link_id:
                link = SocialMediaLink.objects.get(
                    id=link_id, owner=instance.owner
                )
                link.platform = link_data.get('platform', link.platform)
                link.url = link_data.get('url', link.url)
                link.save()
            else:
                SocialMediaLink.objects.create(
                    owner=instance.owner, **link_data
                )

        return instance

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
