from rest_framework import permissions

#Manage permissions for the TournamentItem model
class TournamentPermission(permissions.BasePermission):
    '''Permissions for the TournamentItem model'''
    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']: 
            #Allow everyone
            return True
        elif view.action in ['register', 'unregister']: 
            #Allow only authenticated users
            return request.user.is_authenticated
        elif view.action in ['create', 'update', 'partial_update', 'destroy', 'open_registration', 'api_start', 'api_finish', 'api_get_matches', 'api_submit_scores']:
            #Allow only admin users
            return request.user.is_authenticated and request.user.is_staff
        else:
            #Otherwise, deny permission
            return False