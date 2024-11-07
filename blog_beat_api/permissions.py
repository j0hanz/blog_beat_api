from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Custom permission to allow only owners to edit objects, while read access is unrestricted."""

    def has_object_permission(self, request, view, obj):
        # Allow read-only requests
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions only allowed for the object owner
        return obj.owner == request.user
