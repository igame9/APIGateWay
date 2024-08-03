import requests
from django.http import HttpResponse

TASK_MANAGER_SERVICE_URL = 'http://localhost:8000/'  # !!!


def proxy_to_task_manager(request, path):
    method = request.method

    url = f'{TASK_MANAGER_SERVICE_URL}/{path}'

    headers = {key: value for key, value in request.headers.items() if key.lower() != 'host'}

    data = request.body

    response = requests.request(method, url, headers=headers, data=data, params=request.GET)

    return HttpResponse(
        response.content,
        status=response.status_code,
        content_type=response.headers.get('Content-Type', 'application/json')
    )
