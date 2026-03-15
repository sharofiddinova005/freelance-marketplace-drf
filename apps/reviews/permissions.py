from rest_framework import permissions

class IsProjectClient(permissions.BasePermission):
    """
    Faqat contract client review yozishi mumkin.
    """

    def has_permission(self, request, view):
        return request.user.role == 'client'

    def has_object_permission(self, request, view, obj):
        return obj.contract.client == request.user
