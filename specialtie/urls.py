# apibackend/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()

# Wire up >our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('users/specialties', views.SpecialtiesViewSet.as_view(
        {'post': 'perform_create'}), name='create-institutions-user'),
    path('specialties', views.SpecialtieAPIView.as_view(), name='specialtie-api'),
    path('searchSpecialties', views.searchSpecialties),
    path('specialtiesByUser/<id>', views.get_specialties_users),
##path("register", views.UserRegisterationAPIView.as_view(), name="create-user"),
    #path("login2", views.my_view),
    # path('createUser', views.create),
    # path('deleteUser/<id>', views.destroy),
    # path('updateUser/<id>', views.update)

]
