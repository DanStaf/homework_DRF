from rest_framework.permissions import BasePermission


class IsModeratorClass(BasePermission):
    message = 'Moderators have access to all courses and lessons, but not allowed to delete and create'

    def has_permission(self, request, view):
        return request.user.groups.filter(name='moderators').exists()


class IsOwnerClass(BasePermission):
    message = 'Owners (not moderators) can view, update and delete their courses and lessons'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
