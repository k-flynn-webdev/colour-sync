from django.contrib.auth import get_user_model as user_model
from sheet.models import Sheet
from django.db import models
from django.utils import timezone

User = user_model()


class TimeSync(models.Model):
    """ Time model to control when a sheet is active """

    isActive = models.BooleanField(default=True, blank=False, null=False)
    """ TimeSync current active state """

    DURATION_CHOICES = [
        ('IN', 'Indefinite'),
        ('DY', 'Day'),
        ('WK', 'Week'),
        ('MH', 'Month'),
        ('YR', 'Year'),
    ]
    REPEAT_CHOICES = [
        ('NO', 'None'),
        ('DY', 'Day'),
        ('WK', 'Week'),
        ('MH', 'Month'),
        ('YR', 'Year'),
    ]

    owner = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    """ Owner this Time model affects """
    sheet = models.ForeignKey(Sheet, on_delete=models.CASCADE)
    """ Sheet this Time model affects """
    meta = models.CharField(max_length=255, blank=True, null=True)
    """ Meta information for this Time model """
    date = models.DateField(default=timezone.now, blank=False, null=False)
    """ Time this model becomes active """
    durationType = models.CharField(
        max_length=2,
        default=DURATION_CHOICES[0][0],
        choices=DURATION_CHOICES,
    )
    """ Duration type, enum choice """
    durationVal = models.PositiveBigIntegerField(default=7)
    """ Time duration, in days, default week """

    repeatType = models.CharField(
        max_length=2,
        default=REPEAT_CHOICES[0][0],
        choices=REPEAT_CHOICES,
    )
    """ Repeat type, enum choice """
    repeatVal = models.PositiveSmallIntegerField(default=0)
    """ Repeat value, in days """
    createdAt = models.DateTimeField(auto_now_add=True)
    """ Time model was created """
    updatedAt = models.DateTimeField(auto_now=True)
    """ Time model was updated """

    class Meta:
        db_table = 'time_sync'
        ordering = ['-updatedAt']
