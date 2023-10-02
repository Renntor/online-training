from rest_framework.permissions import BasePermission


class IsStaffViewSet(BasePermission):

    def has_permission(self, request, view):
        if view.action in ['list', 'update', 'create',]:
            return request.user.is_authenticated
        else:
            return request.user.is_superuser


class IsStaff(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True

        return request.user == view.get_object().owner
