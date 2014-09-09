from .serializers import *
from .models import *

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from django.conf import settings
from django.core.cache import caches
from django.http import QueryDict

from bson.objectid import ObjectId

import datetime

cache = caches['default']

class FeaturedList(generics.ListCreateAPIView):
    
	serializer_class = FeaturedSerializer

	def get_queryset(self):
		featured = cache.get('featured')
		if not featured:
			featured = Featured.objects(dateExpired__gt=datetime.datetime.now()).limit(settings.MAX_FEATURED)
			cache.set('featured', featured)
		return featured

	def create(self, request, *args, **kwargs):
		data = request.DATA
		try:
			if type(data) is QueryDict:
				data = dict(data.iterlists())
				for k, v in data.iteritems():
					data[k] = v[0]

			featured = Featured(**data)
			featured.save()
		except ValidationError, e:
			return Response(e.to_dict(), status=status.HTTP_400_BAD_REQUEST)

		return Response(status=status.HTTP_201_CREATED)