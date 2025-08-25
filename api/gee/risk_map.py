# api/gee/risk_map.py
def calculate_risk_map(geometry, start_date, end_date):
    """Mock function for Risk Map calculation"""
    return {
        'risk_score': 0.72,
        'risk_category': 'High',
        'factors': {
            'vegetation_health': 0.65,
            'soil_moisture': 0.58,
            'temperature_anomaly': 0.81,
            'precipitation_deficit': 0.73
        },
        'time_series': [
            {'date': '2020-01-01', 'value': 0.68},
            {'date': '2020-02-01', 'value': 0.69},
            {'date': '2020-03-01', 'value': 0.71},
            {'date': '2020-04-01', 'value': 0.73},
            {'date': '2020-05-01', 'value': 0.75},
            {'date': '2020-06-01', 'value': 0.74},
            {'date': '2020-07-01', 'value': 0.73},
            {'date': '2020-08-01', 'value': 0.72},
            {'date': '2020-09-01', 'value': 0.71},
            {'date': '2020-10-01', 'value': 0.70},
            {'date': '2020-11-01', 'value': 0.69},
            {'date': '2020-12-01', 'value': 0.68},
        ]
    }