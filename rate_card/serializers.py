from rest_framework import serializers
from .models import RateCard, ServiceArea, ServiceCategory, BusinessModel


class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ('id', 'title', 'description')
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }
        read_only_fields = ('created_at', 'updated_at', 'id')


class ServiceAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceArea
        fields = ('id', 'title')
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }
        read_only_fields = ('created_at', 'updated_at', 'id')


class BusinessModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessModel
        fields = ('id', 'title', 'description')
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }
        read_only_fields = ('created_at', 'updated_at', 'id')


class BaseRateCardSerializer(serializers.ModelSerializer):
    business_model = BusinessModelSerializer(read_only=True)
    service_categories = ServiceCategorySerializer(many=True, read_only=True)
    service_areas = ServiceAreaSerializer(many=True, read_only=True)
    class Meta:
        model = RateCard
        fields = "__all__"
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }
        read_only_fields = ('created_at', 'updated_at', 'id', 'archived_at')


class RateCardSerializer(BaseRateCardSerializer):
    business_model_id = serializers.PrimaryKeyRelatedField(
        queryset=BusinessModel.objects.all(),
        source='business_model',
        write_only=True
    )
    service_category_ids = serializers.PrimaryKeyRelatedField(
        queryset=ServiceCategory.objects.all(),
        source='service_categories',
        write_only=True,
        many=True
    )
    service_area_ids = serializers.PrimaryKeyRelatedField(
        queryset=ServiceArea.objects.all(),
        source='service_areas',
        write_only=True,
        many=True
    )
    include_rate_cards = BaseRateCardSerializer(many=True, read_only=True)
    include_rate_card_ids = serializers.PrimaryKeyRelatedField(
        queryset=RateCard.objects.all(),
        source='include_rate_cards',
        write_only=True,
        many=True
    )
    class Meta:
        model = RateCard
        fields = '__all__'
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }
        read_only_fields = ('created_at', 'updated_at', 'id', 'archived_at')
