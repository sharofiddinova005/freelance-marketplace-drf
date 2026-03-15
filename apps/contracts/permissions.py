from rest_framework import permissions

class IsClient(permissions.BasePermission):
    """
    Faqat client freelancer tanlashi mumkin.
    """

    def has_permission(self, request, view):
        return request.user.role == 'client'
