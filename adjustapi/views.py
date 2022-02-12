import csv
import requests
from django.http import JsonResponse
from django.db.models import ExpressionWrapper, F, FloatField, Sum
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework import viewsets
from rest_framework import status

from .models import Datamodel
from .filter import DataFilter
from .serializers import DataSerializer


class ApiViewSet(viewsets.ModelViewSet):
    queryset = Datamodel.objects.all()
    serializer_class = DataSerializer
    filterset_class = DataFilter
    ordering_fields = '__all__'

    def get_queryset(self):
        group_by = self.request.query_params.getlist('group_by')
        cpi = self.request.query_params.getlist('cpi')
        limit = self.request.query_params.getlist('limit')
        if group_by:
            queryset = Datamodel.objects.values(*group_by).annotate(
                clicks=Sum('clicks'),
                impressions=Sum('impressions'),
                installs=Sum('installs'),
                revenue=Sum('revenue'),
                spend=Sum('spend'))
        if cpi:
            queryset = queryset.annotate(cpi=ExpressionWrapper(
                F('spend') / F('installs'), output_field=FloatField()))
        if limit:
            queryset = queryset.values(*group_by, *cpi, *limit)
        return queryset


@api_view(['POST'])
@renderer_classes([BrowsableAPIRenderer])
def csv_upload(request):
    try:
        response = requests.get(request.data)
        data = response.text.splitlines()
        reader = csv.reader(data)
        next(reader, None)
        for row in reader:
            Datamodel.objects.update_or_create(
                date=row[0],
                channel=row[1],
                country=row[2],
                os=row[3],
                impressions=row[4],
                clicks=row[5],
                installs=row[6],
                spend=row[7],
                revenue=row[8],
            )
        return JsonResponse(status.HTTP_200_OK)
    except Exception:
        return JsonResponse(status.HTTP_400_BAD_REQUEST)
  
