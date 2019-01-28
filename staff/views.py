#from django.shortcuts import render
from rest_framework import viewsets
from staff.serializers import StaffSerializer



# Create your views here.
class StaffViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows staffs to be viewed or edited
    """
    queryset = Staff.objects.all().order_by("-updated_at")
    serializer_class = StaffSerializer
