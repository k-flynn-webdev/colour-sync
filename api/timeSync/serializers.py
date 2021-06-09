from rest_framework import serializers
from . import models


class TimeSyncSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TimeSync
        exclude = []
