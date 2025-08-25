# api/gee/urban_heat.py
def calculate_urban_heat(geometry, start_date, end_date):
    """Mock function for Urban Heat Island calculation"""
    return {
        'mean_temperature': 28.5,
        'urban_rural_difference': 3.2,
        'time_series': [
            {'date': '2020-01-01', 'urban': 26.5, 'rural': 23.8},
            {'date': '2020-02-01', 'urban': 27.8, 'rural': 24.5},
            {'date': '2020-03-01', 'urban': 29.2, 'rural': 25.7},
            {'date': '2020-04-01', 'urban': 30.1, 'rural': 26.3},
            {'date': '2020-05-01', 'urban': 30.8, 'rural': 26.9},
            {'date': '2020-06-01', 'urban': 29.7, 'rural': 26.2},
            {'date': '2020-07-01', 'urban': 28.5, 'rural': 25.4},
            {'date': '2020-08-01', 'urban': 27.9, 'rural': 25.0},
            {'date': '2020-09-01', 'urban': 27.3, 'rural': 24.6},
            {'date': '2020-10-01', 'urban': 26.8, 'rural': 24.2},
            {'date': '2020-11-01', 'urban': 26.2, 'rural': 23.9},
            {'date': '2020-12-01', 'urban': 25.7, 'rural': 23.5},
        ]
    }