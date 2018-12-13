# from django.shortcuts import render
from school.models import School
from rest_framework import viewsets
from school.serializers import SchoolSerializer


# Create your views here.
class SchoolViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows schools to be viewed or edited
    """
    queryset = School.objects.all().order_by("-date_updated")
    serializer_class = SchoolSerializer


