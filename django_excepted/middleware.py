class ExceptionHandlingMiddleware(object):
    """
    Handle exceptions nicely, by redirecting to a specific view
    """

    def process_exception(self, request, exception):
        try:
            getattr(exception, "render")
        except AttributeError:
            return None
        
        return exception.render(request)

        return None

