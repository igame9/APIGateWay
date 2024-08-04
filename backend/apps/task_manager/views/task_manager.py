import requests
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.status import HTTP_401_UNAUTHORIZED
from settings.settings import TASK_MANAGER_SERVICE_URL


class TaskManagerProxy(APIView):

    def dispatch(self, request, *args, **kwargs):
        method = request.method
        path = kwargs.get('path', '')

        url = f'{TASK_MANAGER_SERVICE_URL}{path}'

        headers = {key: value for key, value in request.headers.items() if key.lower() != 'host'}

        print(headers)

        auth_header = headers.get("Authorization", None)

        if not auth_header:
            return HttpResponse(
                "Authorization header not found",
                status=HTTP_401_UNAUTHORIZED,
                content_type='application/json'
            )

        data = request.body

        response = requests.request(method, url, headers=headers, data=data, params=request.GET)

        return HttpResponse(
            response.content,
            status=response.status_code,
            content_type=response.headers.get('Content-Type', 'application/json')
        )
