from celery import shared_task

from apps.leads.models import Lead


@shared_task(name="notify_lead_and_attorney")
def notify_lead_and_attorney(lead_id: int):
    """
    Task to notify lead and attorney about the lead submission.
    """
    try:
        lead = Lead.objects.get(id=lead_id)
        lead.notify_lead_and_attorney()
    except Exception as e:
        # Handle the exception (e.g., log it)
        print(f"Error notifying lead and attorney: {e}")
