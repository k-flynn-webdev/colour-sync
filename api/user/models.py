from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    # We don't need to define the email attribute because is inherited from AbstractUser
    meta = models.CharField(max_length=255)
