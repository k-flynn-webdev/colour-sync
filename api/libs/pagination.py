from rest_framework.response import Response
from rest_framework import pagination


class LimitOffsetPagination(pagination.LimitOffsetPagination):

    def get_paginated_response(self, data):
        return Response({
            'count': self.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'detail': None,
            'data': data,
        })
