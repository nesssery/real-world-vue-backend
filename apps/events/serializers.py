from rest_framework import serializers
from apps.events.models import Event, Categorie


# Event Serializers

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


# Categorie Serializers

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = "__all__"
