from rest_framework.permissions import BasePermission


class HasSubscription(BasePermission):
    message = 'User has not subscription or expired'

    def has_permission(self, request, view):
        user = request.user
        return request.user.has_active_subscription()
