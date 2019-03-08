from student.models import Student, Parent, StudentAchievement
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('school_organisation_id', 'first_name', 'last_name','reg_num', 
        'level' , 'level', 'profile_pics',
                  'created_at', 'updated_at')


class ParentSerializer(serializers.ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=Student.objects.all())
    class Meta:
        model = Parent
        fields = ('school_organisation_id', 'students','user_id','home_addr', 'emergency_numbers',
                  'created_at', 'updated_at')


class StudentAchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAchievement
        fields = ('student', 'achievement', 'created_at', 'updated_at')