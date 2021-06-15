from ..models import Location, Provider, Category
from rest_framework import serializers
from rest_framework import viewsets


class InputProviderSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.select_related().all(), source='category_id')
    location = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.select_related().all(), source='location_id')

    class Meta:
        model = Provider
        fields = "__all__"
        depth = 2


class OutputProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = "__all__"
        depth = 2
