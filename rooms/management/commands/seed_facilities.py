from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):

    help = "This Command creates facilities"

    def handle(self, *args, **options):  # 커맨드 실행 시 실행 값
        facilities = [
            "Privatve entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for f in facilities:
            Facility.objects.create(name=f)  # 모듈.오브젝트.명령어()
        self.stdout.write(self.style.SUCCESS(f"facilities {len(facilities)}개가 생성됨."))

