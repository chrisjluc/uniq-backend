from .serializers import *
from .models import *

from rest_framework import generics
from rest_framework.response import Response
from django.conf import settings

class FeaturedList(generics.ListCreateAPIView):
    
	serializer_class = FeaturedSerializer

	def get_queryset(self):
		return Featured.objects.limit(settings.MAX_FEATURED)