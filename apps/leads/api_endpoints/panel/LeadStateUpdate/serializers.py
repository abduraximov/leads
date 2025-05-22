from rest_framework import serializers

from apps.leads.models import Lead


class LeadStateUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for Leads State update
    """

    class Meta:
        model = Lead
        fields = (
            'id',
            'state',
        )

    def to_representation(self, instance):
        """
        Custom representation for the serializer
        """
        representation = super().to_representation(instance)
        representation['state'] = instance.get_state_display()
        return representation

