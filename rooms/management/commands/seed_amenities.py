from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):

    help = "This Command creates amenities"

    def handle(self, *args, **options):  # 커맨드 실행 시 실행 값
        amenities = [
            "Kitchen",
            "Shampoo",
            "Heating",
            "Air-conditioning",
            "Washer",
            "Dryer",
            "Wifi",
            "Breakfast",
            "Indoor fireplace",
            "Hangers",
            "Iron",
            "Hair dryer",
            "Laptop-friendly workspace",
            "TV",
            "Crib",
            "High-chair",
            "Self-checkin",
            "Smoke-alarm",
            "monoxide-alarm",
            "Private-bathroom",
            "Piano",
            "Beachfront",
            "Waterfront",
        ]
        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created!"))
