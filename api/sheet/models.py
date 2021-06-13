from django.contrib.auth import get_user_model as user_model
from django.core.validators import MaxValueValidator
from django.db import models
from project.models import Project

User = user_model()


class Sheet(models.Model):
    name = models.CharField(max_length=255, blank=False, default='')
    url = models.CharField(max_length=255, blank=False, null=False)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    data = models.TextField(blank=True, null=True)
    ranking = models.PositiveSmallIntegerField(default=1, validators=[MaxValueValidator(999)])

    meta = models.CharField(max_length=255, blank=False, default='')

    updatedAt = models.DateTimeField(auto_now_add=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    deletedAt = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'sheets'
        ordering = ['-updatedAt']
