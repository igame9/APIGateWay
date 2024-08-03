"""
URL configuration for settings project.

The `urlpatterns` list routes URLs to proxy. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function proxy
    1. Add an import:  from my_app import proxy
    2. Add a URL to urlpatterns:  path('', proxy.home, name='home')
Class-based proxy
    1. Add an import:  from other_app.proxy import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
