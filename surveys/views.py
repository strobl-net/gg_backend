from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters
from permissions.permissions import IsAdminOrReadOnly
from .models import Survey
from .serializers import SurveySerializer


class SurveyView(viewsets.ModelViewSet):
    permission_classes = [
        IsAdminOrReadOnly
    ]
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'created']
    search_fields = ['name']

    def get_queryset(self):
        return self.queryset.order_by('id')

    def perform_create(self, serializer):
        serializer.save()
