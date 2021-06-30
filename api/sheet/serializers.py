from timeSync.serializers import TimeSyncSerializer
from libs import serlializer_updateAt
from . import models


class SheetSerializer(serlializer_updateAt.CustomSerializerUpdatedAt):
    time_sync_data = TimeSyncSerializer(many=True, read_only=True)
    _locked_fields = ['id', 'owner', 'sheet', 'project']

    class Meta:
        model = models.Sheet
        read_only_fields = ('createdAt', 'updatedAt', 'deletedAt')
        exclude = []
