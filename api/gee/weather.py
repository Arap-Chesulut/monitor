# api/gee/weather.py
def get_weather_data(geometry, start_date, end_date):
    """Mock function for Weather data"""
    return {
        'average_temperature': 24.8,
        'average_humidity': 65.3,
        'time_series': [
            {
                'date': '2020-01-01', 
                'temperature': 23.5, 
                'humidity': 62, 
                'wind_speed': 3.2
            },
            {
                'date': '2020-02-01', 
                'temperature': 24.2, 
                'humidity': 63, 
                'wind_speed': 3.5
            },
            # Add more months as needed
        ]
    }