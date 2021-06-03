from ..models import  Location
from rest_framework import viewsets
from ..serializers.location import *



class LocationView(viewsets.ModelViewSet):
	queryset=Location.objects.all()
	serializer_class=LocationSerializer