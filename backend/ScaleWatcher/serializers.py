from rest_framework import serializers
from .models import ScaleWatcher

class ScaleWatcherSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScaleWatcher
        fields = ('id', 'title', 'description','line')
