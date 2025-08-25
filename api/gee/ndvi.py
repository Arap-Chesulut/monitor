# api/gee/ndvi.py
import json
from datetime import datetime

def calculate_ndvi(geometry, start_date, end_date):
    """
    Mock function for NDVI calculation
    In a real implementation, this would connect to Google Earth Engine
    """
    # For now, return mock data
    return {
        'mean_ndvi': 0.65,
        'time_series': [
            {'date': '2020-01-01', 'value': 0.62},
            {'date': '2020-02-01', 'value': 0.64},
            {'date': '2020-03-01', 'value': 0.67},
            {'date': '2020-04-01', 'value': 0.69},
            {'date': '2020-05-01', 'value': 0.71},
            {'date': '2020-06-01', 'value': 0.68},
            {'date': '2020-07-01', 'value': 0.65},
            {'date': '2020-08-01', 'value': 0.63},
            {'date': '2020-09-01', 'value': 0.61},
            {'date': '2020-10-01', 'value': 0.59},
            {'date': '2020-11-01', 'value': 0.57},
            {'date': '2020-12-01', 'value': 0.55},
        ]
    }