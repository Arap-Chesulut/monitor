# api/gee/water_bodies.py
def calculate_water_bodies(geometry, start_date, end_date):
    """Mock function for Water Bodies detection"""
    return {
        'water_area_km2': 12.5,
        'change_per_year': -0.8,
        'time_series': [
            {'date': '2020-01-01', 'value': 13.3},
            {'date': '2020-02-01', 'value': 13.2},
            {'date': '2020-03-01', 'value': 13.1},
            {'date': '2020-04-01', 'value': 13.0},
            {'date': '2020-05-01', 'value': 12.9},
            {'date': '2020-06-01', 'value': 12.8},
            {'date': '2020-07-01', 'value': 12.7},
            {'date': '2020-08-01', 'value': 12.6},
            {'date': '2020-09-01', 'value': 12.5},
            {'date': '2020-10-01', 'value': 12.4},
            {'date': '2020-11-01', 'value': 12.3},
            {'date': '2020-12-01', 'value': 12.2},
        ]
    }