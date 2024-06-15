# filters.py
import django_filters
from .models import Availability


class AvailabilityFilter(django_filters.FilterSet):
    class Meta:
        model = Availability
        fields = ['date']
