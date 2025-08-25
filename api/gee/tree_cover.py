# api/gee/tree_cover.py
def calculate_tree_cover(geometry, start_date, end_date):
    """Mock function for Tree Cover calculation"""
    return {
        'tree_cover_percentage': 35.7,
        'change_per_year': -1.2,
        'time_series': [
            {'date': '2020-01-01', 'value': 36.9},
            {'date': '2020-02-01', 'value': 36.7},
            {'date': '2020-03-01', 'value': 36.5},
            {'date': '2020-04-01', 'value': 36.3},
            {'date': '2020-05-01', 'value': 36.1},
            {'date': '2020-06-01', 'value': 35.9},
            {'date': '2020-07-01', 'value': 35.7},
            {'date': '2020-08-01', 'value': 35.5},
            {'date': '2020-09-01', 'value': 35.3},
            {'date': '2020-10-01', 'value': 35.1},
            {'date': '2020-11-01', 'value': 34.9},
            {'date': '2020-12-01', 'value': 34.7},
        ]
    }