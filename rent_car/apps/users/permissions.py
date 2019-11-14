from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = 'It is not your account'

    def has_object_permission(self, request, view, obj):
        return obj == request.user