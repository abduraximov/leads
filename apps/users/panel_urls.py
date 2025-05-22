from django.urls import path

from apps.users.api_endpoints import panel

app_name = 'panel_users'

urlpatterns = [
    path('login/', panel.LoginView.as_view(), name='login'),
]