# from django.shortcuts import render
from school.models import School
from school.serializers import SchoolSerializer


# Create your views here.
class SchoolViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows schools to be viewed or edited
    """
    queryset = School.objects.all().order_by("-updated_at")
    serializer_class = SchoolSerializer



