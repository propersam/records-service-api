from record.models import School, Session, Term, Level, Group, Subject
from rest_framework import serializers


class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        fields = ("school_name", "school_website", "about_school", "school_address", "school_phone", "date_created")


class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = ('school', 'session_name', "date_created")


class TermSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Term
        fields = ('session', 'term', 'start_date', 'end_date', "date_created")


class LevelSerializer(serializers.HyperlinkedModelSerializer):
    model = Level
    fields = ('session', 'level_name', "date_created")


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    model = Group
    fields = ('group_name', 'levels', "date_created")


class SubjectSerializer(serializers.ModelSerializer):
    model = Subject
    fields = ('school', 'subject_name', 'description', "date_created")
