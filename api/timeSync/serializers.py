from libs import serlializer_updateAt
from . import models


class TimeSyncSerializer(serlializer_updateAt.CustomSerializerUpdatedAt):
    _locked_fields = ['id', 'owner', 'sheet', 'project']

    class Meta:
        model = models.TimeSync
        read_only_fields = ('createdAt', 'updatedAt', 'deletedAt')
        exclude = []
