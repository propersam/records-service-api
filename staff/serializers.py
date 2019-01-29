from rest_framework import serializers
from staff import models


class StaffLevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StaffLevel
        fields = ('id', 'organisation_id', 'level', 'description', 
        'created_at', 'updated_at')


class StaffPositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StaffPosition
        fields = ('id', 'organisation_id', 'position', 'description',
        'created_at', 'updated_at')


class StaffDepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StaffDepartment
        fields = ('id', 'organisation_id', 'department', 'description',
        'created_at', 'updated_at')


class StaffContractSerializer(serializers.ModelSerializer):
    staff_position_id = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=models.StaffPosition.objects.all())
    staff_department_id = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=models.StaffDepartment.objects.all())
    staff_level_id = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=models.StaffLevel.objects.all())    
    
    class Meta:
        model = models.StaffContract
        fields = (
            'id', 'organisation_id', 'staff_id','staff_position_id',
            'staff_department_id', 'staff_level_id', 'start_date',
            'end_date', 'end_of_trial', 'work_schedule', 'salary', 
            'contract_state', 'created_at', 'updated_at',
            )

