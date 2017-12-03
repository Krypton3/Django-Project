from rest_framework import permissions


class IsOwnerorReadOnly(permissions.BasePermission):
    """
    Custom permission to allow user to edit or create
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
