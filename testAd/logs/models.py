from django.db import models


class LogEvent(models.Model):
    """Model representing a log event."""
    timestamp = models.CharField(max_length=255)
    computer_name = models.CharField(max_length=255)
    event_type = models.CharField(max_length=255)
    application = models.CharField(max_length=255)
    window_title = models.CharField(max_length=255)
    content = models.TextField()
    screenshot_url = models.URLField(max_length=255)
