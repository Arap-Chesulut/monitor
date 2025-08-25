# api/gee/utils.py
import json
from datetime import datetime

def parse_geojson(geojson_str):
    """Parse GeoJSON string to Python dict"""
    if isinstance(geojson_str, str):
        try:
            return json.loads(geojson_str)
        except json.JSONDecodeError:
            return None
    return geojson_str

def validate_dates(start_date, end_date):
    """Validate that start date is before end date"""
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
    
    if start_date > end_date:
        raise ValueError("Start date must be before end date")
    
    return start_date, end_date

def generate_time_series(start_date, end_date, values):
    """Generate a time series with dates and values"""
    # This is a simplified version - in a real implementation,
    # you would generate actual dates based on the date range
    return [{'date': f'2020-{month:02d}-01', 'value': value} 
            for month, value in enumerate(values, 1)]