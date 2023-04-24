from rest_framework.permissions import BasePermission


class IsBoss(BasePermission):
    message = 'permission denied, you are not Boss'
    
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.user_type == 'B':
            return True

class IsVisitor(BasePermission):
    message = 'permission denied, you are not Visitor'
    
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.user_type == 'V':
            return True

class IsCustomer(BasePermission):
    message = 'permission denied, you are not Customer'
    
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.user_type == 'C':
            return True
  