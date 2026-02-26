from django.conf import settings
from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path

from users.views import home


def health_check(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("admin/", admin.site.urls),
    path("health/", health_check, name="health"),
    path("", home, name="home"),
    path("users/", include("users.urls")),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
