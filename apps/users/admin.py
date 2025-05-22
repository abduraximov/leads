from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        "id",
        "username",
        "role",
        "get_full_name",
        "is_deleted"
    )
    search_fields = (
        "username",
        "first_name",
        "last_name",
    )
    readonly_fields = ("created_at", "updated_at")
    list_filter = ("is_deleted", "role")
    ordering = ("-created_at",)
    fieldsets = (
        (None, {"fields": ("password", "username")}),
        (_("Personal info"), {"fields": ("first_name", "last_name",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "role",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            _("User Settings"),
            {
                "fields": (
                    "is_deleted",
                )
            }
        ),

        (_("Important dates"), {"fields": ("last_login", "date_joined", "deleted_at")}),
    )
    # filter_horizontal = ()
    # raw_id_fields = ()
    date_hierarchy = "created_at"

