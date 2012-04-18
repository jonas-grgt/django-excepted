from django.http import HttpResponseNotFound

class CustomException(Exception):
    def render(self):
        return HttpResponseNotFound("Just what you might have expected, not ?")
