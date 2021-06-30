from rest_framework import serializers
from django.utils import timezone

locked_fields = ['id', 'owner', 'sheet', 'project']


class CustomSerializerUpdatedAt(serializers.ModelSerializer):
    """
    - Create a custom serializer that automatically updates the time on the `updatedAt` field
    - Also does some validation checking for `locked_fields`
    """
    def update(self, instance, validated_data):
        temp_locked_fields = locked_fields
        if hasattr(self, '_locked_fields'):
            temp_locked_fields = self._locked_fields

        for item in temp_locked_fields:
            if item in validated_data:
                raise serializers.ValidationError({
                    'detail': 'Not allowed to update: ' + str(item),
                    'data': None
                })

        validated_data['updatedAt'] = timezone.now()
        return super().update(instance, validated_data)
