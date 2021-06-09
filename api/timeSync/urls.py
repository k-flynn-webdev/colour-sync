from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from timeSync import views

urlpatterns = [
    path('', views.TimeSyncList.as_view()),
    path('<int:pk>/', views.TimeSyncDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
