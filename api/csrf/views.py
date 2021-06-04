from django.middleware.csrf import get_token
from django.http import JsonResponse


def get_csrf(request):
    token = get_token(request)
    response = JsonResponse({
        'detail': 'CSRF cookie set',
        'token': token
    })
    response['X-CSRFToken'] = token
    return response
