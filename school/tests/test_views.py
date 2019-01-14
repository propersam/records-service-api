from rest_framework.test import APITestCase, APIClient
from rest_framework.test import APIRequestFactory
from django.urls import reverse
from school.views import SchoolViewSet, StaffViewSet
import json


class SchoolTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = SchoolViewSet.as_view({'get': 'list'})
        self.client = APIClient()

    def test_school_list(self):
        uri = reverse('schools-list')
        response = self.client.get(uri)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'.format(response.status_code))

    def test_school_create(self):
        uri = reverse('schools-list')
        school_data = {
            "school_name": "maggi schools", "school_website": "https://magschl.edu.ng",
            "about_school": "very humble kind of school", "school_address": "locatd where u cn n3v37 find it",
            "school_phone": "08056741987"
        }
        response = self.client.post(uri, school_data)
        self.assertEqual(response.status_code, 201,
                         'Expected Response Code 201, received {0} instead.'.format(response.status_code))

