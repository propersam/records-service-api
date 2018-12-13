from record.models import Session, Term, Level, Group, Subject
from rest_framework import serializers


class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = ('school', 'session_name', "date_created", "date_updated")


class TermSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Term
        fields = ('school', 'term', 'start_date', 'end_date', "date_created", "date_updated")


class LevelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Level
        fields = ('session', 'level_name', "date_created", "date_updated")


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('group_name', 'levels', "date_created", "date_updated")


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('school', 'subject_name', 'description', 'level', 'group', 'date_created', "date_updated")
