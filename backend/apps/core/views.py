from django.http import JsonResponse


def set_csrf(request):
    return JsonResponse({"data": {"message": "CSRF cookie set"}})
