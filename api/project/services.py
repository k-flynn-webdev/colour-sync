from rest_framework import permissions, pagination
from project.serializers import ProjectSerializer
from sheet.serializers import SheetSerializer


def create_basic_sheet(owner=-1, project=-1):
    """ Return data of a basic `Sheet` """
    return {
        'name': 'Base',
        'url': 'Base',
        'owner': owner,
        'project': project,
        'ranking': 1,
        'meta': 'Basic CSS sheet, this will always be the default.',
        'data': '###### BASE CSS ######\n## Place your CSS data here ##',
        'is_base': True
    }


class ProjectService:
    # queryset = Project.objects.all() - overridden with custom func
    permission_classes = (
        permissions.IsAuthenticated,
    )
    serializer_class = ProjectSerializer
    pagination_class = pagination.LimitOffsetPagination

    def create_new_project(self, data):
        """ Handle creating a `Project` and its base `Sheet` """
        project_serializer = ProjectSerializer(data=data)
        project_serializer.is_valid(raise_exception=True)
        project_serializer.save()

        owner = data.get('owner')
        project = project_serializer.data.get('id')

        sheet_serializer = SheetSerializer(data=create_basic_sheet(owner, project))
        sheet_serializer.is_valid(raise_exception=True)
        sheet_serializer.save()

        return project_serializer


