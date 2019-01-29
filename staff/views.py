#from django.shortcuts import render
from rest_framework import viewsets
from staff.serializers import StaffContractSerializer, StaffDepartmentSerializer
from staff.serializers import StaffLevelSerializer, StaffPositionSerializer
from staff import models


# Create your views here.
class StaffDepartmentViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows staffs to be viewed or edited
    """
    queryset = models.StaffDepartment.objects.all().order_by("-updated_at")
    serializer_class = StaffDepartmentSerializer


class StaffLevelViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows staffs to be viewed or edited
    """
    queryset = models.StaffLevel.objects.all().order_by("-updated_at")
    serializer_class = StaffLevelSerializer


class StaffContractViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows staffs to be viewed or edited
    """
    queryset = models.StaffContract.objects.all().order_by("-updated_at")
    serializer_class = StaffContractSerializer


class StaffPostionViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows staffs to be viewed or edited
    """
    queryset = models.StaffPosition.objects.all().order_by("-updated_at")
    serializer_class = StaffPositionSerializer

