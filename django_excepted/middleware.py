from django.core.signals import got_request_exception
from django.dispatch import receiver
import sys
import threading


@receiver(got_request_exception, weak=False)
def got_request_exception(sender, request, **kwargs):
    exc_info = sys.exc_info()
    if getattr(exc_info, 'render', None):
        ExceptionHandlingMiddleware.thread.exc = exc_info


class ExceptionHandlingMiddleware(object):
    """
    Handle exceptions nicely, by redirecting to a specific view.
    """
    # Create a threadlocal variable to store the exception for response.
    thread = threading.local()

    def process_exception(self, request, exception):
        """
        NOTE: does not get called for all exceptions,
        e.g. from view middleware.
        """
        try:
            getattr(exception, "render")
        except AttributeError:
            return None

        return exception.render(request)

    def process_response(self, request, response):
        exc_info = getattr(ExceptionHandlingMiddleware.thread, 'exc_info', None)

        if exc_info:
            # XXX: we might pass in response here
            return exc_info[0].render(exc_info[1], request)

        return response
