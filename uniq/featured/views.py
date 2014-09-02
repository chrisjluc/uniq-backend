from .serializers import *
from .models import *

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

class FeaturedList(generics.ListCreateAPIView):
    
	serializer_class = FeaturedSerializer

	def get_queryset(self):
		return Featured.objects.limit(settings.MAX_FEATURED)

	def create(self, request, *args, **kwargs):
		data = request.DATA
		try:
			featured = Featured(**data)
			featured.save()
		except ValidationError, e:
			return Response(e.to_dict(), status=status.HTTP_400_BAD_REQUEST)
		except:
			return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		return Response(status=status.HTTP_201_CREATED)