from django.urls import path

from apps.leads.api_endpoints import panel


app_name = "panel_leads"

urlpatterns = [
    path("", panel.LeadsView.as_view(), name="leads_list"),
    path("<int:pk>/state/", panel.LeadStateUpdateView.as_view(), name="leads_update"),
]