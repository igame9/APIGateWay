from django.urls import include, path
from .views import set_csrf


urlpatterns = [
    path("api/csrf/", set_csrf, name="csrf"),
]
