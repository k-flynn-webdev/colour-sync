from django.contrib.auth import get_user_model as user_model
from django.apps import apps
from django.db import models

User = user_model()


class Project(models.Model):
    name = models.CharField(max_length=255, blank=False, default='')
    owner = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)

    meta = models.CharField(max_length=255, blank=True, null=True)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    deletedAt = models.DateTimeField(blank=True, null=True)

    @property
    def sheets(self):
        sheet = apps.get_model('sheet.Sheet')
        return sheet.objects.filter(project=self).count()

    class Meta:
        db_table = 'projects'
        ordering = ['-updatedAt']
