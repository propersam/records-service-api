#  from django.shortcuts import render
from .models import Student, StudentAchievement, Parent
from .serializers import StudentSerializer, ParentSerializer, StudentAchievementSerializer
from rest_framework import viewsets


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer


class StudentAchievementViewSet(viewsets.ModelViewSet):
    queryset = StudentAchievement.objects.all()
    serializer_class = StudentAchievementSerializer
