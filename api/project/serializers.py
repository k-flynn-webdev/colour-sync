from rest_framework import serializers
from libs import serlializer_updateAt
from . import models


class ProjectSerializer(serlializer_updateAt.CustomSerializerUpdatedAt):
    sheets = serializers.ReadOnlyField()
    _locked_fields = ['id', 'owner', 'sheet', 'project']

    class Meta:
        model = models.Project
        read_only_fields = ('createdAt', 'updatedAt', 'deletedAt')
        exclude = []
