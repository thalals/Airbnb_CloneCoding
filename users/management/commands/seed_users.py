from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User

# 실험 할 유저 생성하는 COMMAND
class Command(BaseCommand):
    help = "This Command creates many users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many users do you want to create?",
        )

    def handle(self, *args, **options):  # 커맨드 실행 시 실행
        number = options.get("number", 1)  # number를 입력하고, 없을 시 1을 default 값으로.
        seeder = Seed.seeder()
        seeder.add_entity(
            User, number, {"is_staff": False, "is_superuser": False}
        )  # add_entity(Model 명, 숫자 값)
        seeder.execute()  # 적용

        self.stdout.write(self.style.SUCCESS("User created!"))
