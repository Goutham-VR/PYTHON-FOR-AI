# Custom Permission 
from rest_framework.permissions import BasePermission # import

# | Method                    | Checks                               | Example                                        |
# | ------------------------- | ------------------------------------ | ---------------------------------------------- |
# | `has_permission()`        | **User/request-level permission**    | "Can this user access this API?"               |
# | `has_object_permission()` | **Specific object-level permission** | "Can this user access THIS particular object?" |

# 1. has_permission======================================================================================================
# Only Un-Auth req can do get, auth can all req
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET','HEAD','OPTIONS']:
            return True
        return request.user and request.user.is_staff

# Here our rule is any authenticated user can access the api
class IsAuthenticatedUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
    
# Only Un-Auth req can do get, auth can all req
class MyCustomPermissionTwo(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET','HEAD','OPTION']:
            return True
        return request.user.is_authenticated

class NoteCreateCustomPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
#========================================================================================================================

#2. has_object_permission================================================================================================
class NoteManageCustomPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and obj.owner == request.user # here login required and logined user == owner of particular object
#========================================================================================================================
