from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # We don't need to define the email attribute because is inherited from AbstractUser
    meta = models.CharField(max_length=255)

    updatedAt = models.DateTimeField(auto_now_add=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    deletedAt = models.DateTimeField(blank=True, null=True)
