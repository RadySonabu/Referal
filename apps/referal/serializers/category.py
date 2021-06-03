from ..models import  Category
from rest_framework import serializers
from rest_framework import viewsets

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category 
		fields=['id', 'is_active', 'modified_by', 'modified_date', 'name', 'phone_number']