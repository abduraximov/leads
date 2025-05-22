from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.conf import settings

from apps.common.models import BaseModel
from apps.users.models import User


class LeadStatus(models.TextChoices):
    """
    Enumeration for lead status.
    """
    PENDING = "PENDING", _("Pending")
    REACHED_OUT = "REACHED_OUT", _("Reached Out")


class Lead(BaseModel):
    """
    Model representing a lead.
    """
    first_name = models.CharField(_("First Name"), max_length=255)
    last_name = models.CharField(_("Last Name"), max_length=255)
    email = models.EmailField(_("Email"))
    resume = models.FileField(_("Resume/CV"), upload_to="resumes/")
    state = models.CharField(
        _("State"),
        max_length=15,
        choices=LeadStatus.choices,
        default=LeadStatus.PENDING,
    )


    class Meta:
        verbose_name = _("Lead")
        verbose_name_plural = _("Leads")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    def notify_lead_and_attorney(self):
        subject = "Thank you for your submission"
        message = f"Dear {self.first_name}, we have received your lead."
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [self.email])

        attorney_email = Lead.get_attorney_emails()
        subject_attorney = "New lead submitted"
        message_attorney = f"{self.first_name} {self.last_name} submitted a lead."
        send_mail(
            subject_attorney,
            message_attorney,
            settings.DEFAULT_FROM_EMAIL,
            [attorney_email]
        )


    @staticmethod
    def get_attorney_emails():
        """
        Get the list of attorney emails from settings.
        """
        attorney_emails = User.objects.filter(
            role="attorney", email__isnull=False).values_list("email", flat=True)

        return attorney_emails



