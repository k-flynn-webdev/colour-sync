from django.contrib.auth import get_user_model as user_model
from django.apps import apps
from django.db import models

User = user_model()


class Project(models.Model):
    """ Project associated with a User """

    isActive = models.BooleanField(default=True, blank=False, null=False)
    """ Project current active state """
    name = models.CharField(max_length=255, blank=False, default='')
    """ Project name """
    owner = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    """ Project Owner """
    meta = models.CharField(max_length=255, blank=True, null=True)
    """ Meta information for the User """
    url = models.CharField(max_length=255, blank=False, null=False)
    """ Project URL """

    @property
    def sheets(self):
        sheet = apps.get_model('sheet.Sheet')
        return sheet.objects.filter(project=self).count()

    createdAt = models.DateTimeField(auto_now_add=True)
    """ Project model was created """
    updatedAt = models.DateTimeField(auto_now=True)
    """ Project model was updated """
    deletedAt = models.DateTimeField(blank=True, null=True)
    """ Project model was soft deleted """

    class Meta:
        db_table = 'projects'
        ordering = ['-updatedAt']
