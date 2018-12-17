from .models import Student, Parent, StudentAchievement
from rest_framework import serializers


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('school', 'unique_tag', 'first_name', 'last_name', 'enrolled_level', 'current_level',
                  'created_at', 'updated_at')


class ParentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parent
        fields = ('student', 'full_name', 'email', 'phone_num', 'email', 'home_addr', 'emergency_numbers',
                  'created_at', 'updated_at')


class StudentAchievementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentAchievement
        fields = ('student', 'achievement', 'created_at', 'updated_at')