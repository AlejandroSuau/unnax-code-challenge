from django.urls import path, re_path, include
from . import settings

urlpatterns = [
    path("api/", include("task.urls")),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        re_path(r"^__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
