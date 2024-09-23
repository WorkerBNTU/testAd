from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LogEventViewSet

router = DefaultRouter()
router.register(r'logs', LogEventViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
