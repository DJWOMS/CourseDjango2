from django.conf import settings
from django.http import Http404
from django.utils.deprecation import MiddlewareMixin

from pages.views import get_page


class PageFallbackMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if response.status_code != 404:
            return response
        try:
            return get_page(request, request.path_info)
        except Http404:
            return response
        except Exception:
            if settings.DEBUG:
                raise
            return response