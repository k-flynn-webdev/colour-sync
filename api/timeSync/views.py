from timeSync.serializers import TimeSyncSerializer
from rest_framework import generics, permissions
from timeSync.models import TimeSync


class TimeSyncList(generics.ListCreateAPIView):
    queryset = TimeSync.objects.all()
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    serializer_class = TimeSyncSerializer


class TimeSyncDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TimeSync.objects.all()
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    serializer_class = TimeSyncSerializer
