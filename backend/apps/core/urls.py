from django.urls import path, re_path
from .views import set_csrf
from apps.task_manager.views import TaskManagerProxy

urlpatterns = [
    path("api/csrf/", set_csrf, name="csrf"),
    re_path(r'^api/task_manager/(?P<path>.*)$', TaskManagerProxy.as_view()),

]
