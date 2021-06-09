from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from sheet import views

urlpatterns = [
    path('', views.SheetList.as_view()),
    path('<int:pk>/', views.SheetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
