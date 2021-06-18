from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse


class CustomRenderer(JSONRenderer):
    """
    Create a custom standardised response
    [
        detail: 'message',
        data: {} or [],
        pagination: {}
    ]
    """
    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context['response'].status_code

        temp_data = data
        temp_page = None
        temp_detail = None
        # split data into pagination parts
        if data.get('data'):
            temp_data = data.get('data')
            temp_page = {
                'count': data.get('count'),
                'next': data.get('next'),
                'previous': data.get('previous')
            }

        if data.get('detail'):
            temp_detail = data.get('detail')

        data_to_render = create_response(temp_data, status_code, temp_detail)

        if temp_page:
            data_to_render.update(temp_page)

        return super(CustomRenderer, self).render(data_to_render, accepted_media_type, renderer_context)


def create_response(data, status_code, detail):
    """
    Create a standardised response
    [
        status: 'message',
        code: 'number',
        data: '{}|[]',
        detail: 'message',
    ]
    """
    response = {
        'status': 'success',
        'code': status_code,
        'data': data,
        'detail': detail
    }

    is_success = str(status_code).startswith('2') or str(status_code).startswith('3')

    if not is_success:
        response['status'] = 'error'
        response['data'] = None
        try:
            response['detail'] = data['detail']
        except KeyError:
            response['detail'] = data

    return response


def custom_renderer_basic(data_to_render, status_code, detail):
    return JsonResponse(create_response(data_to_render, status_code, detail))
