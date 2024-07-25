from django.contrib.auth.hashers import make_password
from django.core.management import BaseCommand
from django.db import IntegrityError

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            superuser, created = User.objects.get_or_create(
                first_name="Admin",
                last_name="Adminov",
                email="admin@mail.ru",
                password=make_password("8jbag17lj"),
                is_staff=True,
                is_superuser=True,
            )

            if created:
                self.stdout.write(self.style.SUCCESS('User "Admin" was created'))

        except IntegrityError:
            self.stdout.write('User "Admin" was already exists')
