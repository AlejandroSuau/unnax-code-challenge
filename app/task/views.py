from rest_framework import viewsets, mixins

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

from .models import Task
from . import serializers


class CeleryTaskCreateView(viewsets.GenericViewSet,
                           mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           mixins.RetrieveModelMixin):
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer

    @method_decorator(cache_page(60*60*1))
    @method_decorator(vary_on_cookie)
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return serializers.TaskDetailSerializer

        return self.serializer_class
