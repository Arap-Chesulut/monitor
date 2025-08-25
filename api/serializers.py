# api/serializers.py
from rest_framework import serializers
from .models import County, AnalysisRequest, ExportRequest

class CountySerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = ['id', 'name', 'code', 'geometry']

class AnalysisRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalysisRequest
        fields = ['id', 'analysis_type', 'county', 'geometry', 'start_date', 'end_date', 'status', 'result', 'created_at']
        read_only_fields = ['status', 'result', 'created_at']
    
    def validate(self, data):
        # Ensure either county or geometry is provided
        if not data.get('county') and not data.get('geometry'):
            raise serializers.ValidationError("Either county or geometry must be provided.")
        
        return data

class ExportRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExportRequest
        fields = ['id', 'analysis_request', 'export_format', 'file', 'created_at']
        read_only_fields = ['file', 'created_at']