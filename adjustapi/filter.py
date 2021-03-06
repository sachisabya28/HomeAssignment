from django_filters import rest_framework as filters
from .models import Datamodel

class DataFilter(filters.FilterSet):
    class Meta:
        model = Datamodel
        fields = {
            'date': ['gte', 'lte', 'range', 'exact', 'gt', 'lt'],
            'channel': ['exact'],
            'country': ['exact'],
            'os': ['exact'],
    }