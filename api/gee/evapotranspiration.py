# api/gee/evapotranspiration.py
def calculate_et(geometry, start_date, end_date):
    """Mock function for Evapotranspiration calculation"""
    return {
        'mean_et': 5.2,
        'time_series': [
            {'date': '2020-01-01', 'value': 4.8},
            {'date': '2020-02-01', 'value': 5.1},
            {'date': '2020-03-01', 'value': 5.5},
            {'date': '2020-04-01', 'value': 5.7},
            {'date': '2020-05-01', 'value': 5.9},
            {'date': '2020-06-01', 'value': 5.6},
            {'date': '2020-07-01', 'value': 5.3},
            {'date': '2020-08-01', 'value': 5.0},
            {'date': '2020-09-01', 'value': 4.9},
            {'date': '2020-10-01', 'value': 4.7},
            {'date': '2020-11-01', 'value': 4.6},
            {'date': '2020-12-01', 'value': 4.5},
        ]
    }