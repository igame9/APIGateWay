import requests
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


TASK_MANAGER_SERVICE_URL = 'http://localhost:8000/'  # !!!


class TaskManagerProxy(APIView):
    permission_classes = [AllowAny]

    def dispatch(self, request, *args, **kwargs):
        method = request.method
        path = kwargs.get('path', '')

        url = f'{TASK_MANAGER_SERVICE_URL}{path}'

        headers = {key: value for key, value in request.headers.items() if key.lower() != 'host'}

        data = request.body

        response = requests.request(method, url, headers=headers, data=data, params=request.GET)

        return HttpResponse(
            response.content,
            status=response.status_code,
            content_type=response.headers.get('Content-Type', 'application/json')
        )
