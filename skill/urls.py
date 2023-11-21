from django.urls import path, include
from rest_framework import routers
from skill import views

router = routers.DefaultRouter()
router.register(r'skills', views.SkillsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/<int:pk>/skills', views.SkillsViewSet.as_view(
        {'get': 'get_skills_users'}), name='get-skills-user'),
    path('users/skills', views.SkillsViewSet.as_view(
        {'post': 'perform_create'}), name='create-skills-user'),
    path('skills/users', views.SkillsViewSet.as_view(
        {'post': 'perform_link'}), name='link-skills-user'),
    path('skills/<int:skill_id>/users/<int:user_id>', views.SkillsViewSet.as_view(
        {'delete': 'delete_user_skill'}), name='delete-user-skill'),

]
