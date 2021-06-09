from django.db import models


class TimeSync(models.Model):
    timeStart = models.DateTimeField()
    timeDuration = models.PositiveBigIntegerField()

    timeRepeatDay = models.PositiveSmallIntegerField()
    timeRepeatWeek = models.PositiveSmallIntegerField()
    timeRepeatMonth = models.PositiveSmallIntegerField()
    timeRepeatYear = models.PositiveSmallIntegerField()
