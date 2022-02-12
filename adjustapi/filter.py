from django_filters import rest_framework as filters
from .models import Datamodel

class DataFilter(filters.FilterSet):
    class Meta:
        model = Datamodel
        fields = {
        'date': ['gte', 'lte', 'range'],
        'channel': ['exact'],
        'country': ['exact'],
        'os': ['exact'],
    }