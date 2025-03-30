from rest_framework import viewsets
from .models import RateCard
from .serializers import RateCardSerializer
# Create your views here.
class RateCardViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing rate card instances.
    """
    queryset = RateCard.objects.all()
    serializer_class = RateCardSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['milestone', 'service_areas']
    # search_fields = ['name']
    ordering = ['created_at']
