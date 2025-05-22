from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser

from .serializers import LeadsApplySerializer


class LeadsApplyView(CreateAPIView):
    """
    API endpoint for applying for a lead
    """
    serializer_class = LeadsApplySerializer
    permission_classes = (AllowAny,)
    parser_classes = (MultiPartParser,)


__all__ = [
    'LeadsApplyView'
]