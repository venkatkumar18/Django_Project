class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # self.translations = {
        #     "en": {"greeting": "Hello", "header": "Welcome Django!"},
        #     "nl": {"greeting": "Hallo", "header": "Welkom Django!"},
        # }

    def __call__(self, request):
        print("custom middleware before next middleware/view")
        response = self.get_response(request)
        print("custom middleware after response or previous middleware")
        return response

    # def process_template_response(self, request, response):
        # if "nl" in request.META["HTTP_ACCEPT_LANGUAGE"]:
        #     response.context_data["translations"] = self.translations
        #     return response
        # return response
