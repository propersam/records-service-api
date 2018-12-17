from rest_framework import serializers
from school.models import School, Staff


class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        fields = ("school_name", "school_website", "about_school",
                  "school_address", "school_phone", "school_logo", "created_at", "updated_at")


class StaffSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Staff
        fields = ("school", "first_name", "last_name", "gender", "phone", "email", "profile_pics",
                  "date_employed", "date_relieved", "created_at", "updated_at")

