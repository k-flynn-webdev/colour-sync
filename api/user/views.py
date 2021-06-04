from rest_framework.response import Response
from rest_framework.views import APIView

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
            return Response({
                'detail': 'No user logged in.',
                'data': {}
            })

        serializer = CustomUserSerializer(request.user)
        return Response({
            'detail': 'User found.',
            'data': serializer.data
        })

