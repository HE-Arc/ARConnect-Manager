from rest_framework import permissions

class TournamentPermission(permissions.BasePermission):
    '''Permissions for the TournamentItem model'''
    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            return True
        elif view.action in ['register', 'unregister']:
            return request.user.is_authenticated
        elif view.action in ['create', 'update', 'partial_update', 'destroy', 'open_registration', 'api_start', 'api_finish', 'api_get_matches', 'api_submit_scores']:
            return request.user.is_authenticated and request.user.is_staff
        else:
            return False