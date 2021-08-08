from rest_framework import permissions, pagination
from django.core.exceptions import ValidationError
from project.serializers import ProjectSerializer
from sheet.serializers import SheetSerializer
from timeSync.models import TimeSync
from sheet.models import Sheet
import datetime



def create_basic_sheet(owner=-1, project=-1):
    """ Return data of a basic `Sheet` """
    return {
        'name': 'Base',
        'url': 'base',
        'owner': owner,
        'project': project,
        'ranking': 1,
        'meta': 'Basic CSS sheet, this is your first css sheet.',
        'data': '###### BASE CSS ######\n## Place your CSS data here ##',
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

    def create_basic_time_instance(self, sheet):
        """ Return a generic time object for sheets that dont own any """
        return {
            'isActive': True,
            'owner': sheet.owner,
            'sheet_id': sheet.id,
            'date': datetime.date.today(),
            'durationType': 'IN',
            'durationVal': 1,
            'meta': sheet.meta
        }

    def collect_sheets_by_rank(self, project):
        """ Collect all Sheets and return by rank """

        if project is None:
            raise ValidationError('Missing project parameter')

        sheets_query = Sheet.objects.filter(isActive=True, project=project)
        time_query_list = list(
            TimeSync.objects.filter(
                isActive=True,
                sheet__in=sheets_query.values('id')
            ).values())

        # // Create time objects for sheets with no time objects attached
        for sheet_item in sheets_query:
            if len(sheet_item.time_sync_data) < 1:
                new_time = self.create_basic_time_instance(sheet_item)
                time_query_list.append(new_time)

        today = datetime.date.today()
        time_date_list = []

        # // find all times that started in the past or now
        # // AND the duration overlaps today
        for item in time_query_list:
            start_date_test = item['date'] <= today
            end_date = item['date'] + datetime.timedelta(days=item['durationVal'])

            if item['durationType'] is 'IN':
                end_date = datetime.date.today()

            end_date_test = end_date >= today

            if start_date_test and end_date_test:
                time_date_list.append(item)

        # // find / sort by ranking
        sheets_set = []

        for item in time_date_list:
            sheet_is_present = False

            # // check sheet not in results set
            for sheet in sheets_set:
                if sheet.id is item['sheet_id']:
                    sheet_is_present = True
                    break

            if sheet_is_present is True:
                continue

            # // find the actual sheet to add to results set
            for sheet in sheets_query:
                if sheet.id is item['sheet_id']:
                    sheets_set.append(sheet)
                    break

        sheets_set.sort(key=lambda x: (x.ranking, x.createdAt))

        return sheets_set

