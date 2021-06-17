from ..models import Location, Provider, Category
from ..serializers.category import CategorySerializer
from ..serializers.location import LocationSerializer
from rest_framework import serializers
from rest_framework import viewsets


class InputProviderSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.select_related().all(), )
    location_id = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.select_related().all(), )

    class Meta:
        model = Provider
        fields = "__all__"
        depth = 2


class OutputProviderSerializer(serializers.ModelSerializer):
    # category = serializers.PrimaryKeyRelatedField(
    #     queryset=Category.objects.select_related().all(), source='category_id')
    # location = serializers.PrimaryKeyRelatedField(
    #     queryset=Location.objects.select_related().all(), source='location_id')
    # category = serializers.CharField(source='category_id', )
    # location = serializers.CharField(source='location_id', )
    category = CategorySerializer(source='category_id')
    location = LocationSerializer(source='location_id')

    class Meta:
        model = Provider
        fields = ['id', 'is_active', 'modified_by', 'modified_date',
                  'name', 'phone_number', 'category', 'location']
        depth = 2
