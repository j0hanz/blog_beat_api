from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

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
        ]
