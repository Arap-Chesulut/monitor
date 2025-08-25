# api/management/commands/load_counties.py
import os
import json
from django.core.management.base import BaseCommand
from api.models import County

class Command(BaseCommand):
    help = 'Load sample county data'

    def handle(self, *args, **options):
        # Sample data for Kenyan counties
        counties_data = [
            {
                "name": "Nairobi",
                "code": "047",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[36.8219, -1.2921], [36.8219, -1.2921], [36.8219, -1.2921], [36.8219, -1.2921]]]
                }
            },
            {
                "name": "Mombasa",
                "code": "001",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[39.6729, -4.0435], [39.6729, -4.0435], [39.6729, -4.0435], [39.6729, -4.0435]]]
                }
            },
            {
                "name": "Kisumu",
                "code": "042",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[34.7619, -0.1022], [34.7619, -0.1022], [34.7619, -0.1022], [34.7619, -0.1022]]]
                }
            }
        ]

        for county_data in counties_data:
            county, created = County.objects.get_or_create(
                name=county_data['name'],
                defaults={
                    'code': county_data['code'],
                    'geometry': json.dumps(county_data['geometry'])
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created county: {county.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'County already exists: {county.name}'))