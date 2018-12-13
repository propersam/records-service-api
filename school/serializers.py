from rest_framework import serializers
from school.models import School


class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        fields = ("school_name", "school_website", "about_school",
                  "school_address", "school_phone", "date_created", "date_updated")
