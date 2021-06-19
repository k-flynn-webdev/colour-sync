from rest_framework import serializers
from . import models


class ProjectSerializer(serializers.ModelSerializer):
    sheets = serializers.ReadOnlyField()

    class Meta:
        model = models.Project
        exclude = []
