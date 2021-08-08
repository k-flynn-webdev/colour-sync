from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from project import views

urlpatterns = [
    path('', views.ProjectList.as_view()),
    path('<int:pk>/', views.ProjectDetail.as_view()),
    path('style/<str:url>.css', views.ProjectStyle.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
