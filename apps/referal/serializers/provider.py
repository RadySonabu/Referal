from ..models import  Provider
from rest_framework import serializers
from rest_framework import viewsets

class ProviderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Provider 
		fields=['id', 'is_active', 'modified_by', 'modified_date', 'name', 'phone_number', 'category_id', 'location_id']