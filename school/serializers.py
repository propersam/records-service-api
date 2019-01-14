from rest_framework import serializers
from school.models import School, Staff


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):
    schools = SchoolSerializer(many=True)

    class Meta:
        model = Staff
        fields = '__all__'
