from ..models import Location, Provider, Category
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

    class Meta:
        model = Provider
        fields = "__all__"
        depth = 2
