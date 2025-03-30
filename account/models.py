from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Account(AbstractUser):
    class Meta:
        db_table = 'accounts'
    """
    Custom user model that extends the default AbstractUser.
    """
    # Add any additional fields you want here
    pass
