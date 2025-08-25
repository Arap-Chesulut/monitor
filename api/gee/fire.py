# api/gee/fire.py
def detect_fires(geometry, start_date, end_date):
    """Mock function for Fire detection"""
    return {
        'fire_count': 23,
        'burned_area_km2': 15.7,
        'events': [
            {'date': '2020-02-12', 'area_km2': 3.2, 'confidence': 0.87},
            {'date': '2020-05-28', 'area_km2': 5.8, 'confidence': 0.92},
            {'date': '2020-08-15', 'area_km2': 4.1, 'confidence': 0.79},
            {'date': '2020-11-03', 'area_km2': 2.6, 'confidence': 0.85},
        ]
    }