from project.serializers import ProjectSerializer
from rest_framework import generics, permissions
from project.models import Project
from libs import mixins


class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    serializer_class = ProjectSerializer


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    serializer_class = ProjectSerializer
    # renderer_classes = [mixins.CustomRenderer]



# from django.http import JsonResponse
# from rest_framework import mixins
# from rest_framework import generics
# from project.models import Project
#
#
# class ProjectShow(
#     # mixins.RetrieveModelMixin,
# #     mixins.UpdateModelMixin,
# #     mixins.DestroyModelMixin,
#     generics.GenericAPIView):
#
#     queryset = Tag.objects.all()
#     serializer_class = TagDetailSerializer
#     lookup_field = 'value'
#     lookup_url_kwarg = 'value'
#
#     def get(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#
#         return JsonResponse({
#             'detail': 'Successfully found',
#             'results': serializer.data
#         })
#
# #     def patch(self, request, *args, **kwargs):
# #         return self.update(request, *args, **kwargs)
#
# #     def delete(self, request, *args, **kwargs):
# #         return self.destroy(request, *args, **kwargs)
