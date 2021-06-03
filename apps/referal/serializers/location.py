from ..models import  Location
from rest_framework import serializers
from rest_framework import viewsets

class LocationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Location 
		fields=['id', 'is_active', 'modified_by', 'modified_date', 'name']