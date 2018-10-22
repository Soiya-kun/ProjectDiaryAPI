import django_filters
from rest_framework import viewsets, filters

from .models import Day
from .serializers import DaySerializer


class DayViewSet(viewsets.ModelViewSet):
    queryset = Day.objects.all()
    serializer_class = DaySerializer
