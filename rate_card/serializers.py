from rest_framework import serializers
from .models import RateCard

class RateCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateCard
        fields = '__all__'
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }
        read_only_fields = ('created_at', 'updated_at', 'id', 'archived_at')

    def create(self, validated_data):
        rate_card = RateCard.objects.create(**validated_data)
        return rate_card

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.business_model = validated_data.get('business_model', instance.business_model)
        instance.service_categories.set(validated_data.get('service_categories', instance.service_categories.all()))
        instance.service_areas.set(validated_data.get('service_areas', instance.service_areas.all()))
        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['service_categories'] = [category.title for category in instance.service_categories.all()]
        representation['service_areas'] = [area.title for area in instance.service_areas.all()]
        representation['business_model'] = instance.business_model.title
        return representation
