# from django.shortcuts import render
from record.models import School, Session, Level, Term, Subject, Group
from rest_framework import viewsets

from record.serializers import SchoolSerializer, SessionSerializer, LevelSerializer, TermSerializer, \
    SubjectSerializer, GroupSerializer


# Create your views here.
class SchoolViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows schools to be viewed or edited
    """
    queryset = School.objects.all().order_by("date_created")
    serializer_class = SchoolSerializer


class SessionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Session to be viewed or edited
    """
    queryset = Session.objects.all().order_by("date_created")
    serializer_class = SessionSerializer


class TermViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Term to be viewed or edited
    """
    queryset = Term.objets.all().order_by("date_created")
    serializer_class = TermSerializer


class LevelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Level to be viewed or edited
    """
    queryset = Level.objects.all().order_by("date_created")
    serializer_class = LevelSerializer


class SubjectViewSet(viewsets.SubjectViewSet):
    """
    API endpoint that allows Subject to be viewed or edited
    """
    queryset = Subject.objects.all().order_by("date_created")
    serializer_class = SubjectSerializer
