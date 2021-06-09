from django.db import models
from sheet.models import Sheet

class TimeSync(models.Model):
    sheet = models.ForeignKey(Sheet, on_delete=models.CASCADE)
    timeStart = models.DateTimeField()
    timeDuration = models.PositiveBigIntegerField()

    timeRepeatDay = models.PositiveSmallIntegerField()
    timeRepeatWeek = models.PositiveSmallIntegerField()
    timeRepeatMonth = models.PositiveSmallIntegerField()
    timeRepeatYear = models.PositiveSmallIntegerField()
