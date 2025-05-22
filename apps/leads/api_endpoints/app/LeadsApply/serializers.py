from rest_framework import serializers

from apps.leads.models import Lead


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

