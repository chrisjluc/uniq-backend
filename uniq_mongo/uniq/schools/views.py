from rest_framework import generics
from .models import School
from .serializers import SchoolSerializer

class SchoolList(generics.ListCreateAPIView):
    serializer_class = SchoolSerializer

    def get_queryset(self):
        return School.objects
