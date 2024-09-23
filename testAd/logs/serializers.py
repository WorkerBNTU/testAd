from rest_framework import serializers
from .models import LogEvent


class LogEventSerializer(serializers.ModelSerializer):
    """Serializer for LogEvent model."""
    class Meta:
        model = LogEvent
        fields = '__all__'
