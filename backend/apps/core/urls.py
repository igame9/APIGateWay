from django.urls import path, re_path
from .views import set_csrf
from apps.task_manager.proxy import proxy_to_task_manager

urlpatterns = [
    path("api/csrf/", set_csrf, name="csrf"),
    re_path(r'^api/task_manager/(?P<path>.*)$', proxy_to_task_manager),

]
