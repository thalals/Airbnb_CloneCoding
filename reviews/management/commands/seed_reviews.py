import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from reviews import models as review_models

from users import models as user_models
from rooms import models as room_models


class Command(BaseCommand):
    help = "This Command creates many review"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many review do you want to create?",
        )

    def handle(self, *args, **options):  # 커맨드 실행 시 실행
        number = options.get("number")
        seeder = Seed.seeder()

        users = user_models.User.objects.all()  # 외래키 설정
        rooms = room_models.Room.objects.all()  # 외래키 설정

        seeder.add_entity(
            review_models.Review,
            number,
            {
                "accuracy": lambda x: random.randint(1, 5),
                "communication": lambda x: random.randint(1, 5),
                "cleanliness": lambda x: random.randint(1, 5),
                "location": lambda x: random.randint(1, 5),
                "check_in": lambda x: random.randint(1, 5),
                "value": lambda x: random.randint(1, 5),
                "user": lambda x: random.choice(users),  # 외래키 설정법
                "room": lambda x: random.choice(rooms),  # 외래키 설정법
            },
        )
        seeder.execute()  # 적용시키기 (필수)
        self.stdout.write(self.style.SUCCESS(f"{number} Review created!"))
