from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status, filters
from rest_framework.renderers import JSONRenderer

from . import serializers
from . import models


class GetTODO(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = serializers.TODOSerializer
    queryset = models.TODO.objects.all()


class CreateTODO(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = serializers.TODOSerializer


class UpdateTODO(generics.UpdateAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = serializers.TODOSerializer
    queryset = models.TODO.objects.all()


class DeleteTODO(generics.DestroyAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = serializers.TODOSerializer
    queryset = models.TODO.objects.all()


class SearchTODO(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = serializers.TODOSerializer
    queryset = models.TODO.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['state', 'date', 'title', 'priority']
    search_fields = ['state', 'date', 'title', 'priority']
