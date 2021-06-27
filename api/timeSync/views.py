from rest_framework import generics, permissions, status
from timeSync.serializers import TimeSyncSerializer
from rest_framework.response import Response
from timeSync.models import TimeSync
from libs import mixins, pagination


class TimeSyncList(generics.ListCreateAPIView):
    # queryset = TimeSync.objects.all() - overridden with custom func
    permission_classes = (
        permissions.IsAuthenticated,
    )
    serializer_class = TimeSyncSerializer
    renderer_classes = [mixins.CustomRenderer]
    pagination_class = pagination.LimitOffsetPagination

    def get_queryset(self):
        return TimeSync.objects.filter(owner=self.request.user)

    def post(self, request, *args, **kwargs):
        temp_data = request.data
        temp_data['owner'] = request.user.id
        serializer = TimeSyncSerializer(data=temp_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)


class TimeSyncDetail(generics.RetrieveUpdateDestroyAPIView):
    # queryset = TimeSync.objects.all() - overridden with custom func
    permission_classes = (
        permissions.IsAuthenticated,
    )
    serializer_class = TimeSyncSerializer
    renderer_classes = [mixins.CustomRenderer]

    def get_queryset(self):
        return TimeSync.objects.filter(owner=self.request.user)
