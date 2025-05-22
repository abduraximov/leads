from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .schema import swagger_urlpatterns



urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/panel/users/", include("apps.users.panel_urls", namespace="panel_users")),
    path("api/v1/leads/", include("apps.leads.urls", namespace="leads")),
    path("api/v1/panel/leads/", include("apps.leads.panel_urls", namespace="panel_leads")),

]

urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
