from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Student, Parent, StudentAchievement


# class StudentTests(APITestCase):
#     def test_create_student(self):
#         """
#         Ensure we can create student a new student object.
#         """
#
#         url = reverse('student-list')
#
#         data = {
#             'school_id': 1, 'unique_tag': 'stud042', 'first_name': 'Jack', 'last_name': 'Sterlings'
#         }
#
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Student.objects.count(), 1)
#         self.assertEqual(Student.objects.get().unique_tag, 'stud042')

