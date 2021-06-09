from rest_framework import serializers
from . import models


class SheetSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Sheet
        exclude = []
