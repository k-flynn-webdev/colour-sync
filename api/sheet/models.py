from django.contrib.auth import get_user_model as user_model
from django.core.validators import MaxValueValidator
from project.models import Project
from django.apps import apps
from django.db import models

User = user_model()


class Sheet(models.Model):
    """ Sheet of different styles a User can assign to a Project """
    name = models.CharField(max_length=255, blank=False, default='')
    """ Sheet name """
    url = models.CharField(max_length=255, blank=False, null=False)
    """ Sheet URL """
    owner = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    """ Sheet Owner """
    project = models.ForeignKey(Project, blank=False, null=False, on_delete=models.CASCADE)
    """ Project this Sheet belongs to """
    data = models.TextField(blank=True, null=True)
    """ Data this Sheet supplies """
    ranking = models.PositiveSmallIntegerField(default=1, validators=[MaxValueValidator(999)])
    """ Sheet ranking vs other Sheets 1 - 999 """
    meta = models.CharField(max_length=255, blank=True, null=True)
    """ Meta information for the User """
    is_base = models.BooleanField(blank=False, null=False, default=False)
    """ Projects Base sheet """

    @property
    def time_sync_data(self):
        """ Sheet TimeSync models """
        time_sync = apps.get_model('timeSync.TimeSync')
        return time_sync.objects.filter(sheet=self.id)

    createdAt = models.DateTimeField(auto_now_add=True)
    """ Sheet model was created """
    updatedAt = models.DateTimeField(auto_now=True)
    """ Sheet model was updated """
    deletedAt = models.DateTimeField(blank=True, null=True)
    """ Sheet model was soft deleted """

    class Meta:
        db_table = 'sheets'
        ordering = ['-updatedAt']
