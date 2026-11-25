"""URL configuration."""

from pathlib import Path

from django.conf import settings
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, re_path


def spa(_request):
    index = Path(settings.FRONTEND_DIR) / "index.html"
    if not index.is_file():
        return HttpResponse("Frontend not built.", status=503)
    return HttpResponse(index.read_text(encoding="utf-8"), content_type="text/html")


urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r"^.*$", spa, name="spa"),
]
