from rest_framework import viewsets
from rest_framework.response import Response
from .models import RateCard, BusinessModel, ServiceCategory, ServiceArea
from .serializers import RateCardSerializer, BusinessModelSerializer, ServiceCategorySerializer, ServiceAreaSerializer


class RateCardViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing rate card instances.
    """
    queryset = RateCard.latest.all()
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


class ServiceCategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing service model instances.
    """
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['milestone', 'service_areas']
    # search_fields = ['name']
    ordering = ['created_at']


class ServiceAreaViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing service area instances.
    """
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer
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
            "service_categories": [{"value": x.id, "label": x.title} for x in ServiceCategory.objects.all()],
            "service_areas": [{"value": x.id, "label": x.title} for x in ServiceArea.objects.all()],
            "business_models": [{"value": x.id, "label": x.title} for x in BusinessModel.objects.all()],
            "price_units": [{"value": x[0], "label": x[1]} for x in RateCard.UNIT_CHOICES],
            "rate_cards": [{"value": x.id, "label": f"{x.get_milestone_display()}: {x.title}"} for x in RateCard.latest.all()],
        })
