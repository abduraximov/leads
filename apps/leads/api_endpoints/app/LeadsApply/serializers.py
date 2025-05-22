from rest_framework import serializers

from apps.leads.models import Lead
from apps.leads.tasks import notify_lead_and_attorney


class LeadsApplySerializer(serializers.ModelSerializer):
    """
    Serializer for Leads Apply
    """
    class Meta:
        model = Lead
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'resume',
            'state',
        )

        extra_kwargs = {
            'state': {'read_only': True},
        }

    def create(self, validated_data):
        """
        Create a new lead instance and notify the lead and attorney.
        """
        lead = Lead.objects.create(**validated_data)
        # Notify the lead and attorney background
        notify_lead_and_attorney.delay(lead.id)
        return lead

