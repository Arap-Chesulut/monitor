# api/admin.py
from django.contrib import admin
from .models import County, AnalysisRequest, ExportRequest

@admin.register(County)
class CountyAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'created_at']

@admin.register(AnalysisRequest)
class AnalysisRequestAdmin(admin.ModelAdmin):
    list_display = ['analysis_type', 'county', 'start_date', 'end_date', 'status']
    list_filter = ['analysis_type', 'status']

@admin.register(ExportRequest)
class ExportRequestAdmin(admin.ModelAdmin):
    list_display = ['analysis_request', 'export_format', 'created_at']