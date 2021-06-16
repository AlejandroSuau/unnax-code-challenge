from django.urls import path, include

from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register("read", views.CeleryTaskCreateView)

app_name = "task"

urlpatterns = [
    path("", include(router.urls)),
]
