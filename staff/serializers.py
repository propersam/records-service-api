from rest_framework import serializers
from staff.models import Staff
from school.models import School


class StaffSerializer(serializers.ModelSerializer):
   school_id = serializers.PrimaryKeyRelatedField(many=False, read_only=False, get_queryset=School.objects.all())
    class Meta:
        model = Staff
        fields = ('school_id', 'first_name', 'last_name', 'gender', 'phone', 'email', 'address', 'profile_pics', 'created_at', 'updated_at')

