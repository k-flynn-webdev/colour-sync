from sheet.serializers import SheetSerializer
from rest_framework import generics, permissions
from sheet.models import Sheet
from libs import mixins, pagination


class SheetList(generics.ListCreateAPIView):
    queryset = Sheet.objects.all()
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    serializer_class = SheetSerializer
    renderer_classes = [mixins.CustomRenderer]
    pagination_class = pagination.LimitOffsetPagination


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sheet.objects.all()
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    serializer_class = SheetSerializer
    renderer_classes = [mixins.CustomRenderer]
