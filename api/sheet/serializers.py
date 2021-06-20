from rest_framework import serializers
from . import models


class SheetSerializer(serializers.ModelSerializer):
    # projectData = serializers.ReadOnlyField()

    class Meta:
        model = models.Sheet
        exclude = []
