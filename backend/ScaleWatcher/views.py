from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ScaleWatcherSerializer
from .models import ScaleWatcher

# Create your views here.

class ScaleWatcherView(viewsets.ModelViewSet):
    serializer_class=ScaleWatcherSerializer
    queryset=ScaleWatcher.objects.all()
