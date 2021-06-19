from django.contrib.auth import get_user_model as user_model
from django.db import models

User = user_model()


class Project(models.Model):
    name = models.CharField(max_length=255, blank=False, default='')
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    meta = models.CharField(max_length=255, blank=True, null=True)

    updatedAt = models.DateTimeField(auto_now_add=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    deletedAt = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'projects'
        ordering = ['-updatedAt']
