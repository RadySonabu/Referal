from ..models import Provider
from rest_framework import viewsets
from ..serializers.provider import *
from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework import status
from ..serializers.provider import InputProviderSerializer, OutputProviderSerializer


class ProviderView(viewsets.ModelViewSet):
    queryset = Provider.objects.select_related(
    ).order_by('-modified_date').all()
    serializer_class = InputProviderSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('name', 'phone_number', 'modified_date',
                        'modified_by', 'is_active', 'category_id__id', 'location_id__id')

    def get_serializer_class(self):
        input_serializer = InputProviderSerializer
        output_serializer = OutputProviderSerializer
        if self.action == 'list':
            return output_serializer
        if self.action == 'retrieve':
            return output_serializer
        if self.action == 'create':
            return input_serializer
        if self.action == 'update':
            return input_serializer

        # I dont' know what you want for create/destroy/update.
        return output_serializer
