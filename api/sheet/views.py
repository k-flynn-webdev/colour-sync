from sheet.serializers import SheetSerializer
from rest_framework import generics, permissions
from sheet.models import Sheet


class SheetList(generics.ListCreateAPIView):
    queryset = Sheet.objects.all()
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    serializer_class = SheetSerializer


class SheetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sheet.objects.all()
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    serializer_class = SheetSerializer
