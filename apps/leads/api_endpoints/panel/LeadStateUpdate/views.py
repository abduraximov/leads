from rest_framework.generics import UpdateAPIView


from .serializers import LeadStateUpdateSerializer
from apps.users.permissions import IsAttorney
from apps.leads.models import Lead


class LeadStateUpdateView(UpdateAPIView):
    """
    API endpoint for updating the state of a lead for attorneys
    """
    serializer_class = LeadStateUpdateSerializer
    queryset = Lead.objects.all()
    permission_classes = (IsAttorney,)
    http_method_names = ('patch',)


__all__ = [
    'LeadStateUpdateView'
]