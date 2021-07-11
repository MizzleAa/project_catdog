from .models import User
from rest_framework.permissions import BasePermission


class LoginRequired(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role_id)


class AdminRequired(BasePermission):
    def has_permission(self, request, view):
        if request.user.role_id == 1:
            result = True
        else:
            result = False

        return bool(request.user and result)