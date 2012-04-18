class CustomException(Exception):
    def render(self):
        return HttpResponseNotFound("foobar")
