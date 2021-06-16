from django.middleware.csrf import get_token
from django.http import JsonResponse
from rest_framework import generics, permissions
from libs.mixins import custom_renderer_basic


def get_csrf(request):
    data = get_token(request)
    response = custom_renderer_basic(data, 200, 'CSRF cookie set')
    response['X-CSRFToken'] = data
    return response

