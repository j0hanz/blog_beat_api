from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    """Serializer for the current authenticated user.
    Extends the user details with profile-related fields.
    """

    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.SerializerMethodField()

    def get_profile_image(self, obj):
        # Safely retrieves profile image URL, returns None if unavailable
        return getattr(getattr(obj.profile, 'image', None), 'url', None)

    class Meta(UserDetailsSerializer.Meta):
        fields = (
            *UserDetailsSerializer.Meta.fields,
            'profile_id',
            'profile_image',
        )
