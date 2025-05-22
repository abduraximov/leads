from django.urls import path

from apps.leads.api_endpoints import app
from apps.leads.api_endpoints import panel


app_name = "leads"

urlpatterns = [
    path("apply/", app.LeadsApplyView.as_view(), name="leads_apply"),
]