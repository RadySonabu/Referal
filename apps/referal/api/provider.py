from ..models import  Provider
from rest_framework import viewsets
from ..serializers.provider import *



class ProviderView(viewsets.ModelViewSet):
	queryset=Provider.objects.all()
	serializer_class=ProviderSerializer