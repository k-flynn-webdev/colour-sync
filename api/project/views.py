from project.serializers import ProjectSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.http import HttpResponse
from libs import mixins, pagination
from project.models import Project
from django.http import Http404
from sheet.models import Sheet
from project import services


class ProjectList(generics.ListCreateAPIView, services.ProjectService):
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

        temp_project = services.create_new_project(temp_data)
        headers = self.get_success_headers(temp_project.data)
        return Response(temp_project.data, status=status.HTTP_200_OK, headers=headers)


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Project.objects.all() - overridden with custom func
    permission_classes = (
        permissions.IsAuthenticated,
    )
    serializer_class = ProjectSerializer
    renderer_classes = [mixins.CustomRenderer]

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)


class ProjectStyle(generics.RetrieveAPIView, services.ProjectService):
    # queryset = Project.objects.all() - overridden with custom func
    permission_classes = (
        permissions.AllowAny,
    )
    serializer_class = ProjectSerializer
    renderer_classes = [mixins.CustomRenderer]
    lookup_field = 'url'

    def get(self, request, *args, **kwargs):
        sheets_data = []
        style_url = self.kwargs.get('url', None)

        # // base is a protected term
        if style_url == 'base':
            raise Http404

        project_found = Project.objects.filter(url=style_url)

        if project_found.first() is not None:
            sheets_data = services.collect_sheets_by_rank(project_found.first())
        else:
            sheets_data = Sheet.objects.filter(url=style_url)

        if len(sheets_data) < 1:
            raise Http404

        # services.create_file(style_url, sheets_data[0].data)

        return HttpResponse(content=sheets_data[0].data, content_type='text/css')

