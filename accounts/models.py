from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    # generate a unique username every time a user is registered
    username = models.CharField(default=uuid.uuid4(), unique=True, max_length = 120)
