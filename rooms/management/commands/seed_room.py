import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):
    help = "This Command creates many room"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many room do you want to create?",
        )

    def handle(self, *args, **options):  # 커맨드 실행 시 실행
        number = options.get("number")  # number를 입력하고, 없을 시 1을 default 값으로.
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "guestes": lambda x: random.randint(1, 3),
                "price": lambda x: random.randint(1, 5),
                "beds": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
            },
        )  # add_entity(Model 명, 생성 할 숫자 값)
        created_photos = seeder.execute()  # 적용
        created_clean = flatten(list(created_photos.values()))  # ID 반환
        amenities = room_models.Amenity.objects.all()
        facilites = room_models.Facility.objects.all()
        rules = room_models.House_rules.objects.all()
        for pk in created_clean:
            # 해당 ROOM PK 값을 가져와서 room_obj 저장
            room_obj = room_models.Room.objects.get(pk=pk)
            for i in range(3, random.randint(10, 30)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room_obj,
                    file=f"/room_photos/{random.randint(1, 31)}.webp",
                )
            for a in amenities:  # N:M 관계에서의 추가 방법.
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room_obj.amenity.add(a)

            for f in facilites:  # N:M 관계에서의 추가 방법.
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room_obj.facility.add(f)

            for r in rules:  # N:M 관계에서의 추가 방법.
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room_obj.house_rules.add(r)

        self.stdout.write(self.style.SUCCESS(f"{number} Room created!"))
