from .models import Student, Parent, StudentAchievement
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('school', 'unique_tag', 'first_name', 'last_name', 'level',
                  'created_at', 'updated_at')


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ('student', 'full_name', 'email', 'phone_num', 'email', 'home_addr', 'emergency_numbers',
                  'created_at', 'updated_at')


class StudentAchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAchievement
        fields = ('student', 'achievement', 'created_at', 'updated_at')