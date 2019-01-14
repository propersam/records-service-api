from record.models import Session, Term, Level, Group, Subject
from rest_framework import serializers


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ('school', 'session_name', "created_at", "updated_at")


class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = ('school', 'term', 'start_date', 'end_date', "created_at", "updated_at")


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('session', 'level_name', "created_at", "updated_at")


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('group_name', 'level', "created_at", "updated_at")


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('school', 'subject_name', 'description', 'levels', 'groups', 'created_at', "updated_at")
