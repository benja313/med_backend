# apibackend/urls.py
from django.urls import include, path
from rest_framework  import routers
from . import views


router = routers.DefaultRouter()

# Wire up >our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('users/', views.index),
    #path('createUser', views.create),
    #path('deleteUser/<id>', views.destroy),
    #path('updateUser/<id>', views.update)

]