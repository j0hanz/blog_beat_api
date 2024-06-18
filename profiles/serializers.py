from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin
from .models import Profile, SocialMediaLink
from followers.models import Follower


class SocialMediaLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaLink
        fields = ['platform', 'url']

    def validate_url(self, value):
        if not value.startswith(('http://', 'https://')):
            raise serializers.ValidationError(
                "URL must start with http:// or https://"
            )
        return value


class ProfileSerializer(CountryFieldMixin, serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    social_media_links = SocialMediaLinkSerializer(many=True, required=False)

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
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

    def create(self, validated_data):
        social_media_links_data = validated_data.pop('social_media_links', [])
        profile = Profile.objects.create(**validated_data)
        for link_data in social_media_links_data:
            SocialMediaLink.objects.create(profile=profile, **link_data)
        return profile

    def update(self, instance, validated_data):
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
        instance.social_media_links.all().delete()
        for link_data in social_media_links_data:
            SocialMediaLink.objects.create(profile=instance, **link_data)
        return instance
