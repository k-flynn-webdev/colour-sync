from timeSync.serializers import TimeSyncSerializer
from rest_framework import generics, permissions
from timeSync.models import TimeSync
from libs import mixins, pagination


class TimeSyncList(generics.ListCreateAPIView):
    queryset = TimeSync.objects.all()
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    serializer_class = TimeSyncSerializer
    renderer_classes = [mixins.CustomRenderer]
    pagination_class = pagination.LimitOffsetPagination


class TimeSyncDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TimeSync.objects.all()
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    serializer_class = TimeSyncSerializer
    renderer_classes = [mixins.CustomRenderer]
