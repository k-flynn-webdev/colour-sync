from project.serializers import ProjectSerializer
from rest_framework import generics, permissions
from project.models import Project
from libs import mixins, pagination


class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    serializer_class = ProjectSerializer
    renderer_classes = [mixins.CustomRenderer]
    pagination_class = pagination.LimitOffsetPagination


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    serializer_class = ProjectSerializer
    renderer_classes = [mixins.CustomRenderer]
