# from django.shortcuts import render
from record.models import Session, Level, Term, Subject, Group
from rest_framework import viewsets

from record.serializers import SessionSerializer, LevelSerializer, TermSerializer, \
    SubjectSerializer, GroupSerializer


# Create your views here.
class SessionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Session to be viewed or edited
    """
    queryset = Session.objects.all().order_by("updated_at")
    serializer_class = SessionSerializer


class TermViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Term to be viewed or edited
    """
    queryset = Term.objects.all().order_by("updated_at")
    serializer_class = TermSerializer


class LevelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Level to be viewed or edited
    """
    queryset = Level.objects.all().order_by("updated_at")
    serializer_class = LevelSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Subject to be viewed or edited
    """
    queryset = Subject.objects.all().order_by("updated_at")
    serializer_class = SubjectSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows Group to be viewed or edited
        """
    queryset = Group.objects.all().order_by("updated_at")
    serializer_class = GroupSerializer
