from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.users.manager import UserManager


class UserRole(models.TextChoices):
    SUPER_ADMIN = "super_admin", _("Super Admin")
    ATTORNEY = "attorney", _("Attorney")
    CLIENT = "client", _("Client")


class User(AbstractUser, BaseModel):

    role = models.CharField(
        max_length=50,
        choices=UserRole.choices,
        verbose_name=_("Role"),
        null=True,
        blank=True,
    )

    is_deleted = models.BooleanField(verbose_name=_("Is deleted"), default=False)
    deleted_at = models.DateTimeField(verbose_name=_("Deleted at"), null=True, blank=True)



    objects = UserManager()
    REQUIRED_FIELDS = []  # type: ignore

    def __str__(self):
        return str(self.username)