from rest_framework import routers
from record import views as record_views
from school import views as school_views
from pupil import views as student_views


router = routers.DefaultRouter()
router.register(r'schools', school_views.SchoolViewSet, base_name='school')
router.register(r'staffs', school_views.StaffViewSet, base_name='staff')
router.register(r'academic-sessions', record_views.SessionViewSet, base_name='academic')
router.register(r'academic-terms', record_views.TermViewSet, base_name='term')
router.register(r'school-levels', record_views.LevelViewSet, base_name='level')
router.register(r'school-subjects', record_views.SubjectViewSet, base_name='subject')
router.register(r'school-groups', record_views.GroupViewSet, base_name='group')
router.register(r'students', student_views.StudentViewSet, base_name='student')
router.register(r'parents', student_views.ParentViewSet, base_name='parent')
router.register(r'student-achievements', student_views.StudentAchievementViewSet, base_name='student_achievement')
