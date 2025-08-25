# api/gee/floods.py
def detect_floods(geometry, start_date, end_date):
    """Mock function for Flood detection"""
    return {
        'flooded_area_km2': 8.3,
        'severity_index': 0.65,
        'events': [
            {'date': '2020-04-15', 'area_km2': 8.3, 'severity': 0.65},
            {'date': '2020-07-22', 'area_km2': 5.1, 'severity': 0.42},
            {'date': '2020-10-08', 'area_km2': 3.7, 'severity': 0.31},
        ]
    }