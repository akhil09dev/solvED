from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BoardViewSet, SolutionViewSet, QuestionViewSet, GradeViewSet, SubjectViewSet, ChapterViewSet

router = DefaultRouter()
router.register(r'boards', BoardViewSet)
router.register(r'solutions', SolutionViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'grades', GradeViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'chapters', ChapterViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Include all auto-generated routes
]
