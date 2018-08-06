from . import views
from rest_framework import routers


from django.urls import path, include
from .views import CoresDashboardView, CourseListView, CourseDetailView, CourseCreateView, CourseUpdateView, CourseDeleteView, SubjectDetailView, SubjectCreateView, SubjectUpdateView, SubjectDeleteView, \
    UnitDetailView, UnitCreateView, UnitUpdateView, UnitDeleteView, ChapterCreateView, ChapterUpdateView, ChapterDeleteView


app_name = 'core'

urlpatterns = [
    path('', CoresDashboardView.as_view(), name='cores_dashboard'),
    path('course-list', CourseListView.as_view(), name='course_list'),
    path('course-detail/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('course-add/', CourseCreateView.as_view(), name='course_add'),
    path('course-edit/<int:pk>/', CourseUpdateView.as_view(), name='course_edit'),
    path('course-delete/<int:pk>/', CourseDeleteView.as_view(), name='course_delete'),

    path('subject-detail/<int:pk>/', SubjectDetailView.as_view(), name='subject_detail'),
    path('subject-add/<int:course_id>/', SubjectCreateView.as_view(), name='subject_add'),
    path('subject-edit/<int:pk>/', SubjectUpdateView.as_view(), name='subject_edit'),
    path('subject-delete/<int:pk>/', SubjectDeleteView.as_view(), name='subject_delete'),

    path('unit-detail/<int:pk>/', UnitDetailView.as_view(), name='unit_detail'),
    path('unit-add/<int:subject_id>/', UnitCreateView.as_view(), name='unit_add'),
    path('unit-edit/<int:pk>/', UnitUpdateView.as_view(), name='unit_edit'),
    path('unit-delete/<int:pk>/', UnitDeleteView.as_view(), name='unit_delete'),

    path('chapter-add/<int:pk>', ChapterCreateView.as_view(), name='chapter_add'),
    path('chapter-edit/<int:pk>/', ChapterUpdateView.as_view(), name='chapter_edit'),
    path('chapter-delete/<int:pk>/', ChapterDeleteView.as_view(), name='chapter_delete'),

    path('question-sets-add/<int:chapter_id>', views.QuestionSetsFormView.as_view(), name='question_sets_add'),
    path('question-sets/<int:chapter_id>', views.QuestionSetsListView.as_view(), name='question_sets'),
    path('question-sets-update/<int:pk>', views.QuestionSetsUpdateView.as_view(), name='question_sets_update'),
    path('question-sets-delete/<int:pk>', views.QuestionSetsDeleteView.as_view(), name='question_sets_delete'),

    path('question-set-dashboard/<int:pk>', views.QuestionSetsDashboard.as_view(), name='question_set_dashboard'),
    path('question-add/<int:pk>', views.QuestionAddView.as_view(), name='question_add'),
    path('question-dashboard/<int:pk>', views.QuestionDashboardView.as_view(), name='question_dashboard'),

    path('option-detail/<int:pk>', views.OptionDetailView.as_view(), name='option_detail'),
    path('option-add/<int:pk>', views.OptionAddView.as_view(), name='option_add'),

    path('signup/', views.SignUp.as_view(), name='signup'),
    path('accounts/user-profile/<username>', views.UserProfileView.as_view(), name='user_profile'),
    path('accounts/user-profile-update/<int:pk>', views.UserProfileUpdateView.as_view(), name='user_profile_update'),  
]
