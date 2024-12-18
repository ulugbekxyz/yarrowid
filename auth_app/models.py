from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Добавьте свои дополнительные поля, если они есть
    phone_number = models.CharField(max_length=15, blank=True, null=True)
