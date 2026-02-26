from django.http import HttpResponse, HttpRequest

class MaintenanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        is_maintenance = False

        if is_maintenance:
            if request.path.startswith("/admin"):
                return self.get_response(request)

            if request.user.is_authenticated and request.user.is_staff:
                return self.get_response(request)

            return HttpResponse("<h1>Under Maintenance</h1>")

        return self.get_response(request)