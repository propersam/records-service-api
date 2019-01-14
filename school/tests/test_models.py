from django.test import TestCase
from ..models import School, Staff
from datetime import date


class SchoolTestCase(TestCase):
    """ This class defines the Model Test suites for School Model """

    def setUp(self):
        # test data for school model
        self.school_name = 'Ransome Kuti Grammer School'
        self.school_website = 'https://ransomekutischool.edu.ng'
        self.about_school = 'A very touch and no non-sense taking school'
        self.school_address = "67, macaul crescent moshalashi mushin, jibowu Lagos"
        self.school_phone = '08041971994'

        # Test Data for Staff model
        # self.school2 = School.objects.get(id=1)
        self.first_name = 'Sodiq'
        self.last_name = 'Hassan'
        self.gender = 'M'
        self.phone = '07055078897'
        self.email = 'propersam2012@example.com'
        self.date_employed = date.today()

    def create_school_model(self):
        """ Test clients and other Test variables for School Model are defined here  """

        return School.objects.create(
            school_name=self.school_name, school_address=self.school_address, about_school=self.about_school,
            school_website=self.school_website, school_phone=self.school_phone
        )

    def create_staff_model(self):

        school = self.create_school_model()
        return Staff.objects.create(
            school_id=school.id, first_name=self.first_name, last_name=self.last_name,
            gender=self.gender, phone=self.phone, email=self.email, date_employed=self.date_employed
        )

    def test_model_can_create_school(self):
        """ Test the School Model can create new School record """
        school = self.create_school_model()
        self.assertEqual(str(school), school.school_name)
        print('New school record added successfully')
        print('[info] school model working fine.')

    def test_model_can_create_staff(self):
        """ Test the Staff Model Can create New Staff Record """
        staff = self.create_staff_model()
        print('New Staff record added successfully')
        self.assertEqual(str(staff), "{} {}".format(staff.last_name, staff.first_name))
        print('Staff model working very fine')


# class StaffModelTestCase(TestCase):
#     """ This class Defines the Model Test suites for Staff Model """
#     # pass
#     def setUp(self):





