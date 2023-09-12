from rest_framework.permissions import BasePermission

class PublicAccessPermission(BasePermission):
    def has_permission(self, request, view):
        return True