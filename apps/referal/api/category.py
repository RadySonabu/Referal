from ..models import  Category
from rest_framework import viewsets
from ..serializers.category import *



class CategoryView(viewsets.ModelViewSet):
	queryset=Category.objects.all()
	serializer_class=CategorySerializer