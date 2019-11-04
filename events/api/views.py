from events.models import Event
from .serializers import EventSerializer
from rest_framework import viewsets


class EventSerializerViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
