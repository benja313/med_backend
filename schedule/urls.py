from django.urls import path, include
from rest_framework import routers
from schedule import views

router = routers.DefaultRouter()
router.register(r'schedules', views.ScheduleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/<int:pk>/schedules/', views.ScheduleViewSet.as_view(
        {'get': 'get_schedules_users'}), name='get-schedules-user'),
    path('users/<int:schedule_professional_id>/schedules', views.ScheduleViewSet.as_view(
        {'put': 'perform_update'}), name='update-schedules-user')

]
