from django.contrib.sessions.models import Session

class ClearSessionsMiddleware:
    _cleared_sessions = False 

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not ClearSessionsMiddleware._cleared_sessions:
            Session.objects.all().delete()
            ClearSessionsMiddleware._cleared_sessions = True
        response = self.get_response(request)
        return response
