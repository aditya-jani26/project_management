
from rest_framework import permissions

class CanCreateProjectPermission(permissions.BasePermission):
    def has_permission(self, request):
        user_type = getattr(request.user, 'userType', None)
        return user_type in ['Admin', 'Project-Manager', 'Team-Leader']

