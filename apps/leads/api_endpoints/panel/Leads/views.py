from rest_framework.generics import ListAPIView


from .serializers import LeadsSerializer
from apps.users.permissions import IsAttorney
from apps.leads.models import Lead


class LeadsView(ListAPIView):
    """
    API endpoint for listing leads for attorneys
    """
    serializer_class = LeadsSerializer
    queryset = Lead.objects.all()
    permission_classes = (IsAttorney,)


__all__ = [
    'LeadsView'
]