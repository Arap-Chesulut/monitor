# api/models.py
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.db import models as django_models

class County(django_models.Model):
    name = django_models.CharField(max_length=100)
    code = django_models.CharField(max_length=10, unique=True)
    geometry = django_models.TextField()  # Store GeoJSON as text
    created_at = django_models.DateTimeField(auto_now_add=True)
    updated_at = django_models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Counties"

    def __str__(self):
        return self.name

class AnalysisRequest(django_models.Model):
    ANALYSIS_TYPES = [
        ('NDVI', 'NDVI Analysis'),
        ('ET', 'Evapotranspiration'),
        ('URBAN_HEAT', 'Urban Heat Island'),
        ('TREE_COVER', 'Tree Cover'),
        ('WATER', 'Water Bodies'),
        ('FLOOD', 'Flood Detection'),
        ('FIRE', 'Fire Detection'),
        ('RAINFALL', 'Rainfall'),
        ('WEATHER', 'Weather Data'),
        ('RISK', 'Risk Map'),
    ]
    
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed'),
    ]
    
    user = django_models.ForeignKey(User, on_delete=django_models.CASCADE, null=True, blank=True)
    analysis_type = django_models.CharField(max_length=20, choices=ANALYSIS_TYPES)
    county = django_models.ForeignKey(County, on_delete=django_models.CASCADE, null=True, blank=True)
    geometry = django_models.TextField(null=True, blank=True)  # Store GeoJSON as text
    start_date = django_models.DateField()
    end_date = django_models.DateField()
    status = django_models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    result = django_models.JSONField(null=True, blank=True)
    created_at = django_models.DateTimeField(auto_now_add=True)
    updated_at = django_models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.analysis_type} - {self.county or 'Custom AOI'} - {self.start_date} to {self.end_date}"

class ExportRequest(django_models.Model):
    FORMAT_CHOICES = [
        ('GEOJSON', 'GeoJSON'),
        ('CSV', 'CSV'),
        ('GEOTIFF', 'GeoTIFF'),
        ('PNG', 'PNG'),
        ('PDF', 'PDF Report'),
    ]
    
    analysis_request = django_models.ForeignKey(AnalysisRequest, on_delete=django_models.CASCADE)
    export_format = django_models.CharField(max_length=10, choices=FORMAT_CHOICES)
    file = django_models.FileField(upload_to='exports/', null=True, blank=True)
    created_at = django_models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.analysis_request.analysis_type} - {self.export_format}"