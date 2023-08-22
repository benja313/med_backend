from django.urls import path, include
from rest_framework import routers
from institution import views

router = routers.DefaultRouter()
router.register(r'institutions', views.InstitutionViewSet)

urlpatterns = [
    path('', include(router.urls))
]
