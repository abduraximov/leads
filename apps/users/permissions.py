from rest_framework import permissions
from django.utils.translation import gettext_lazy as _

from .models import UserRole


class IsAttorney(permissions.BasePermission):
    """
    Custom permission to only allow attorneys to access the view.
    """
    message = _("Only attorneys can access this.")

    def has_permission(self, request, view):
        user = request.user
        if user.is_authenticated and user.role == UserRole.ATTORNEY:
            return True
        return False

