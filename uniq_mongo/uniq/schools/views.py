from rest_framework import generics
from .models import School
from .serializers import SchoolSerializer
from uniq.exceptions import CouldNotBeFoundException

class SchoolList(generics.ListCreateAPIView):
    serializer_class = SchoolSerializer

    def get_queryset(self):
        return School.objects.all()

class SchoolDetail(generics.RetrieveAPIView):
	serializer_class = SchoolSerializer

	def get_object(self):
		pk = int(self.kwargs['pk'])
		try:
			return School.objects.filter(school_id=pk)[:1].get()
		except:
			raise CouldNotBeFoundException()