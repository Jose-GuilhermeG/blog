#imports
from rest_framework.permissions import BasePermission,SAFE_METHODS

#permissios
class IsUserOwnerOrReadOnly(BasePermission):
    """
        Check if user is owner of object 
    """
    
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        return request.user == obj.user
        