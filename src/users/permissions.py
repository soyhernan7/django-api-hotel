"""User permission classes."""

# Django REST Framework
from rest_framework.permissions import BasePermission

# Models
from src.users.models import User


class IsStandardUser(BasePermission):
    """Allow access to create dif modules"""

    def has_permission(self, request, view):

        try:
            user = User.objects.get(
                email=request.user,
                is_recruiter=False
            )
        except User.DoesNotExist:
            return False
        return True


class IsRecruiterUser(BasePermission):
    """Allow access to search rooms."""

    def has_permission(self, request, view):

        try:
            user = User.objects.get(
                email=request.user,
                is_recruiter=True
            )
        except User.DoesNotExist:
            return False
        return True