from django.db import models
from sheet.models import Sheet


class TimeSync(models.Model):
    """ Time model to control when a sheet is active """

    sheet = models.ForeignKey(Sheet, on_delete=models.CASCADE)
    """ Sheet this time model affects """
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
    updatedAt = models.DateTimeField(auto_now_add=True)
    """ Time model was updated """
    createdAt = models.DateTimeField(auto_now_add=True)
    """ Time model was created """

    class Meta:
        db_table = 'time_sync'
        ordering = ['-updatedAt']
