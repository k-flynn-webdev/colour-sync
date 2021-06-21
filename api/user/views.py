from rest_framework.response import Response
from rest_framework.views import APIView
from libs.mixins import custom_renderer_basic

from .serializers import CustomUserSerializer


class WhoAmIView(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = []

    @staticmethod
    def get(request, format=None):
        try:
            request.user.meta
        except Exception as e:
            return custom_renderer_basic({}, 200, 'No user logged in.')

        serializer = CustomUserSerializer(request.user)
        return custom_renderer_basic(serializer.data, 200, 'User found.')

