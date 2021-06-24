from django.contrib.auth import get_user_model as user_model
from django.db import models
from sheet.models import Sheet

User = user_model()


class TimeSync(models.Model):
    """ Time model to control when a sheet is active """
    owner = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    """ Owner this time model affects """
    sheet = models.ForeignKey(Sheet, on_delete=models.CASCADE)
    """ Sheet this time model affects """
    meta = models.CharField(max_length=255, blank=True, null=True)
    """ Meta information for the User """
    timeStart = models.DateTimeField()
    """ Time this model becomes active """
    timeDuration = models.PositiveBigIntegerField(default=7)
    """ Time duration, in days, default week """

    REPEAT_CHOICES = [
        ('NO', 'None'),
        ('DY', 'Day'),
        ('WK', 'Week'),
        ('MH', 'Month'),
        ('YR', 'Year'),
    ]
    repeatType = models.CharField(
        max_length=2,
        default='NO',
        choices=REPEAT_CHOICES,
    )
    """ Repeat time, enum choice """
    repeatVal = models.PositiveSmallIntegerField(default=0)
    """ Repeat value, in days """
    createdAt = models.DateTimeField(auto_now_add=True)
    """ Time model was created """
    updatedAt = models.DateTimeField(auto_now_add=True)
    """ Time model was updated """

    class Meta:
        db_table = 'time_sync'
        ordering = ['-updatedAt']
