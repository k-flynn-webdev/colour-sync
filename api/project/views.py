from project.serializers import ProjectSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from libs import mixins, pagination
from project.models import Project


class ProjectList(generics.ListCreateAPIView):
    # queryset = Project.objects.all() - overridden with custom func
    permission_classes = (
        permissions.IsAuthenticated,
    )
    serializer_class = ProjectSerializer
    renderer_classes = [mixins.CustomRenderer]
    pagination_class = pagination.LimitOffsetPagination

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)

    def post(self, request, *args, **kwargs):
        temp_data = request.data
        temp_data['owner'] = request.user.id
        serializer = ProjectSerializer(data=temp_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Project.objects.all() - overridden with custom func
    permission_classes = (
        permissions.IsAuthenticated,
    )
    serializer_class = ProjectSerializer
    renderer_classes = [mixins.CustomRenderer]

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)
