from django.db import models
from django.utils import timezone


class Datamodel(models.Model):
    date = models.DateField(default=timezone.now)
    channel = models.CharField(max_length=150)
    country = models.CharField(max_length=2)
    os = models.CharField(max_length=100)
    impressions = models.IntegerField()
    clicks = models.IntegerField()
    installs = models.IntegerField()
    spend = models.FloatField()
    revenue = models.FloatField()
    
    def __str__(self):
        return self.country
