from record.models import Session, Term, Level, Group, Subject
from rest_framework import serializers


class SessionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Session
        fields = ('school_organisation_id', 'session', "created_at", "updated_at")


class TermSerializer(serializers.ModelSerializer):

    class Meta:
        model = Term
        fields = ('school_organisation_id', 'term', 'start_date', 'end_date', "created_at", "updated_at")


class LevelSerializer(serializers.ModelSerializer):
    session_id = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=Session.objects.all())

    class Meta:
        model = Level
        fields = ('school_organisation_id', 'session_id', 'level', "created_at", "updated_at")


class GroupSerializer(serializers.ModelSerializer):
    level_id = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=Level.objects.all())

    class Meta:
        model = Group
        fields = ('school_organisation_id', 'group', 'level_id', "created_at", "updated_at")


class SubjectSerializer(serializers.ModelSerializer):
    levels = serializers.StringRelatedField(many=True,)
    groups = serializers.StringRelatedField(many=True,)

    class Meta:
        model = Subject
        fields = ('school_organisation_id', 'subject', 'description', 'levels', 'groups', 'created_at', "updated_at")
