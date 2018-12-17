# from django.shortcuts import render
from school.models import School, Staff
from rest_framework import viewsets
from school.serializers import SchoolSerializer, StaffSerializer


# Create your views here.
class SchoolViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows schools to be viewed or edited
    """
    queryset = School.objects.all().order_by("-updated_at")
    serializer_class = SchoolSerializer


class StaffViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows staffs to be viewed or edited
    """
    queryset = Staff.objects.all().order_by("-updated_at")
    serializer_class = StaffSerializer



