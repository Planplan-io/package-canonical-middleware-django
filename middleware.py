from django.utils.deprecation import MiddlewareMixin
from django.utils.cache import patch_vary_headers
from django.http import HttpRequest, HttpResponse

class CannonicalMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        super().__init__(get_response)
        self.redirect = True
        

    def process_response(self, request: HttpRequest, response: HttpResponse) -> HttpResponse:
        patch_vary_headers(response, ('Accept-Encoding',))

        if response.status_code <= 400 and request.accepts('text/html'):
                response.headers['Link'] = f'<{request.build_absolute_uri(request.path)}>; rel="canonical"'
                
        return response
