from rest_framework import generics, permissions, status
from sheet.serializers import SheetSerializer
from rest_framework.response import Response
from libs import mixins, pagination
from sheet.models import Sheet


class SheetList(generics.ListCreateAPIView):
    # queryset = Sheet.objects.all() - overridden with custom func
    permission_classes = (
        permissions.IsAuthenticated,
    )
    serializer_class = SheetSerializer
    renderer_classes = [mixins.CustomRenderer]
    pagination_class = pagination.LimitOffsetPagination

    def get_queryset(self):
        return Sheet.objects.filter(owner=self.request.user)

    def post(self, request, *args, **kwargs):
        temp_data = request.data
        temp_data['owner'] = request.user.id
        serializer = SheetSerializer(data=temp_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)


class SheetDetail(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Sheet.objects.all()
    permission_classes = (
        permissions.IsAuthenticated,
    )
    serializer_class = SheetSerializer
    renderer_classes = [mixins.CustomRenderer]

    def get_queryset(self):
        return Sheet.objects.filter(owner=self.request.user)

