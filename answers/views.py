from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters

from .models import Answer
from .serializers import AnswerSerializer


class AnswerView(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny
    ]
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['survey_id', 'user_id']
    search_fields = ['survey_id', 'user_id']

    def get_queryset(self):
        return self.queryset.order_by('id')
