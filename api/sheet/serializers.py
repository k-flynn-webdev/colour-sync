from rest_framework import serializers
from timeSync.serializers import TimeSyncSerializer
from . import models


class SheetSerializer(serializers.ModelSerializer):
    time_sync_data = TimeSyncSerializer(many=True, read_only=True)

    class Meta:
        model = models.Sheet
        exclude = []
