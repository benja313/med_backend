from django.urls import path, include
from rest_framework import routers
from institution import views

router = routers.DefaultRouter()
router.register(r'institutions', views.InstitutionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/<int:pk>/institutions', views.InstitutionViewSet.as_view(
        {'get': 'get_queryset'}), name='get-institutions-user'),
    path('users/institutions', views.InstitutionViewSet.as_view(
        {'post': 'perform_create'}), name='create-institutions-user'),
]
