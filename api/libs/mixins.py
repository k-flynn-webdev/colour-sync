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
    def render(self, data, accepted_media_type=None, renderer_context=None, detail=None):
        status_code = renderer_context['response'].status_code

        temp_data = data
        temp_page = None
        # split data into pagination parts
        if data.get('data'):
            temp_data = data.get('data')
            temp_page = {
                'count': data.get('count'),
                'next': data.get('next'),
                'previous': data.get('previous')
            }

        detail_found = detail
        if hasattr(self, 'detail'):
            detail_found = self.detail

        response = create_response(temp_data, status_code, detail_found)

        if temp_page:
            response.update(temp_page)
            print(temp_page)

        return super(CustomRenderer, self).render(response, accepted_media_type, renderer_context)


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


def custom_renderer_basic(data, status_code, detail):
    return JsonResponse(create_response(data, status_code, detail))
