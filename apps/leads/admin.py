from django.contrib import admin

from . import models


@admin.register(models.Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'email',
        'state',
        'created_at',
        'updated_at',
    )

    search_fields = (
        'first_name',
        'last_name',
        'email',
    )
