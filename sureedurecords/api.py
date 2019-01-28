from rest_framework import routers
from record import views as record_views
from student import views as student_views


router = routers.DefaultRouter()
router.register(r'academic-sessions', record_views.SessionViewSet, base_name='sessions')
router.register(r'academic-terms', record_views.TermViewSet, base_name='terms')
router.register(r'school-levels', record_views.LevelViewSet, base_name='levels')
router.register(r'school-subjects', record_views.SubjectViewSet, base_name='subjects')
router.register(r'school-groups', record_views.GroupViewSet, base_name='groups')
router.register(r'students', student_views.StudentViewSet, base_name='students')
router.register(r'parents', student_views.ParentViewSet, base_name='parents')
router.register(r'student-achievements', student_views.StudentAchievementViewSet, base_name='student_achievements')
