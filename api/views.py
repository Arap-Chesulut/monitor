# api/views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from .models import County, AnalysisRequest, ExportRequest
from .serializers import CountySerializer, AnalysisRequestSerializer, ExportRequestSerializer
from .gee import (
    ndvi, evapotranspiration, urban_heat, tree_cover, 
    water_bodies, floods, fire, rainfall, weather, risk_map
)

class CountyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = County.objects.all()
    serializer_class = CountySerializer

class AnalysisRequestViewSet(viewsets.ModelViewSet):
    queryset = AnalysisRequest.objects.all()
    serializer_class = AnalysisRequestSerializer
    
    def perform_create(self, serializer):
        analysis_request = serializer.save()
        # Process synchronously for now (replace with Celery later)
        self.process_analysis(analysis_request.id)
    
    def process_analysis(self, analysis_id):
        analysis = AnalysisRequest.objects.get(id=analysis_id)
        
        try:
            analysis.status = 'PROCESSING'
            analysis.save()
            
            # Process based on analysis type
            if analysis.analysis_type == 'NDVI':
                result = ndvi.calculate_ndvi(
                    analysis.geometry, 
                    analysis.start_date.isoformat(), 
                    analysis.end_date.isoformat()
                )
            elif analysis.analysis_type == 'ET':
                result = evapotranspiration.calculate_et(
                    analysis.geometry, 
                    analysis.start_date.isoformat(), 
                    analysis.end_date.isoformat()
                )
            elif analysis.analysis_type == 'URBAN_HEAT':
                result = urban_heat.calculate_urban_heat(
                    analysis.geometry, 
                    analysis.start_date.isoformat(), 
                    analysis.end_date.isoformat()
                )
            elif analysis.analysis_type == 'TREE_COVER':
                result = tree_cover.calculate_tree_cover(
                    analysis.geometry, 
                    analysis.start_date.isoformat(), 
                    analysis.end_date.isoformat()
                )
            elif analysis.analysis_type == 'WATER':
                result = water_bodies.calculate_water_bodies(
                    analysis.geometry, 
                    analysis.start_date.isoformat(), 
                    analysis.end_date.isoformat()
                )
            elif analysis.analysis_type == 'FLOOD':
                result = floods.detect_floods(
                    analysis.geometry, 
                    analysis.start_date.isoformat(), 
                    analysis.end_date.isoformat()
                )
            elif analysis.analysis_type == 'FIRE':
                result = fire.detect_fires(
                    analysis.geometry, 
                    analysis.start_date.isoformat(), 
                    analysis.end_date.isoformat()
                )
            elif analysis.analysis_type == 'RAINFALL':
                result = rainfall.calculate_rainfall(
                    analysis.geometry, 
                    analysis.start_date.isoformat(), 
                    analysis.end_date.isoformat()
                )
            elif analysis.analysis_type == 'WEATHER':
                result = weather.get_weather_data(
                    analysis.geometry, 
                    analysis.start_date.isoformat(), 
                    analysis.end_date.isoformat()
                )
            elif analysis.analysis_type == 'RISK':
                result = risk_map.calculate_risk_map(
                    analysis.geometry, 
                    analysis.start_date.isoformat(), 
                    analysis.end_date.isoformat()
                )
            else:
                raise ValueError(f"Unknown analysis type: {analysis.analysis_type}")
            
            # Save result
            analysis.result = result
            analysis.status = 'COMPLETED'
            analysis.save()
            
        except Exception as e:
            analysis.status = 'FAILED'
            analysis.result = {'error': str(e)}
            analysis.save()
    
    @action(detail=True, methods=['post'])
    def export(self, request, pk=None):
        analysis_request = self.get_object()
        export_format = request.data.get('format', 'GEOJSON')
        
        export_request = ExportRequest.objects.create(
            analysis_request=analysis_request,
            export_format=export_format
        )
        
        # For now, just return the export request
        serializer = ExportRequestSerializer(export_request)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ExportRequestViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ExportRequest.objects.all()
    serializer_class = ExportRequestSerializer
    
    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        export_request = self.get_object()
        # For now, return a simple response
        return Response({"message": "Export functionality not yet implemented"})