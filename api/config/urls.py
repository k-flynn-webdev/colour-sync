"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static, serve

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('accounts/admin/', admin.site.urls),
    path('api/csrf/', include('csrf.urls')),
    path('api/whoami/', include('user.urls')),
    path('project/', include('project.urls')),
    path('sheet/', include('sheet.urls')),
    path('timesync/', include('timeSync.urls')),
]
              # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# if settings.DEBUG: