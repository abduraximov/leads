from rest_framework import serializers

from apps.leads.models import Lead


class LeadsSerializer(serializers.ModelSerializer):
    """
    Serializer for Leads list
    """
    state = serializers.CharField(source='get_state_display', read_only=True)

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

