from rest_framework import permissions

class IsFreelancer(permissions.BasePermission):
    """
    Faqat freelancer bid yuborishi mumkin.
    """

    def has_permission(self, request, view):
        return request.user.role == 'freelancer'

