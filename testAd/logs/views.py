from rest_framework import viewsets
from .models import LogEvent
from .serializers import LogEventSerializer


class LogEventViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for viewing log events."""
    queryset = LogEvent.objects.all()
    serializer_class = LogEventSerializer
