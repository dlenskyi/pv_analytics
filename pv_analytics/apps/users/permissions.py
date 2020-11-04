from rest_framework.permissions import BasePermission


class IsAuthenticated(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        if request.user.id is None:
            return False
        return (
            request.user
            and request.user.is_authenticated
            and request.user.is_active
        )
