from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class LoginMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path_info in ['/login/', '/image/code/']:
            return None

        session_info = request.session.get('info')
        if not session_info:
            return redirect('/login/')

    def process_response(self, request, response):
        return response
