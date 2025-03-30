from rest_framework import viewsets
from rest_framework.response import Response
from .models import RateCard, BusinessModel
from .serializers import RateCardSerializer, BusinessModelSerializer
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


class BusinessModelViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing business model instances.
    """
    queryset = BusinessModel.objects.all()
    serializer_class = BusinessModelSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['milestone', 'service_areas']
    # search_fields = ['name']
    ordering = ['created_at']

class OptionsViewset(viewsets.ViewSet):
    """
    A viewset for viewing and editing options instances.
    """

    def list(self, request):
        """
        List all options.
        """
        return Response({
            "milestones": [{"value": x[0], "label": x[1]} for x in RateCard.MILESTONE_CHOICES],
            # "service_categories": ServiceCategorySerializer(ServiceCategory.objects.all(), many=True).data,
            # "service_areas": ServiceAreaSerializer(ServiceArea.objects.all(), many=True).data,
            "business_models": [{"value": x.id, "label": x.title} for x in BusinessModel.objects.all()]
        })
