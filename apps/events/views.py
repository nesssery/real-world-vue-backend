from rest_framework import viewsets, permissions
from apps.events.models import Event, Categorie
from apps.events.serializers import EventSerializer, CategorieSerializer


# Event serializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EventSerializer


class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CategorieSerializer
