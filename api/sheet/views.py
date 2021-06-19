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

    def post(self, request, *args, **kwargs):
        # //    todo override serilizer class for creation of an object replacing
        # //    `owner` with request.user
        # //    I wanna use the DRF way if possible
        return self.create(request, *args, **kwargs)


class SheetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sheet.objects.all()
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    serializer_class = SheetSerializer
    renderer_classes = [mixins.CustomRenderer]
