from django.core.management.base import BaseCommand, CommandError
from django.core.management import utils

class Command(BaseCommand):
    help = 'Generate a new secret key for the Django project'
    env_file_path = '.env'

    def add_arguments(self, parser):
        parser.add_argument(
            '--env',
            type=str,
            default=self.env_file_path,
            help='Path to the environment file where the secret key will be set.',
        )

    def handle(self, *args, **kwargs):
        secret_key = utils.get_random_secret_key()
        self.set_key_in_environment_file(secret_key)
        print(f"Secret key set successfully.")

    def set_key_in_environment_file(self, key):
        try:
            with open(self.env_file_path, 'r') as file:
                lines = file.readlines()

            with open(self.env_file_path, 'w') as file:
                for line in lines:
                    if line.startswith('SECRET_KEY'):
                        file.write(f'SECRET_KEY="{key}"\n')
                    else:
                        file.write(line)
        except FileNotFoundError:
            raise CommandError(f"Environment file {self.env_file_path} not found.")
