from rest_framework.permissions import BasePermission


class IsModeratorClass(BasePermission):
    message = 'Moderators have access to all courses and lessons, but not allowed to delete and create'

    def has_permission(self, request, view):
        return request.user.groups.filter(name='moderators').exists()
