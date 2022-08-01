from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Agency api',
        default_version='v1',
        description='For agency rest api',
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('agency_api.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
