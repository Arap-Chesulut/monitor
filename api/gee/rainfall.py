# api/gee/rainfall.py
def calculate_rainfall(geometry, start_date, end_date):
    """Mock function for Rainfall calculation"""
    return {
        'total_rainfall_mm': 845,
        'average_monthly_mm': 70.4,
        'time_series': [
            {'date': '2020-01-01', 'value': 45},
            {'date': '2020-02-01', 'value': 52},
            {'date': '2020-03-01', 'value': 78},
            {'date': '2020-04-01', 'value': 125},
            {'date': '2020-05-01', 'value': 142},
            {'date': '2020-06-01', 'value': 98},
            {'date': '2020-07-01', 'value': 63},
            {'date': '2020-08-01', 'value': 47},
            {'date': '2020-09-01', 'value': 56},
            {'date': '2020-10-01', 'value': 72},
            {'date': '2020-11-01', 'value': 89},
            {'date': '2020-12-01', 'value': 78},
        ]
    }