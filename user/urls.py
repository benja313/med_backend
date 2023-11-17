# apibackend/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()

# Wire up >our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('users', views.index),
    path("login", views.UserLoginAPIView.as_view(), name="login-user"),
    path("register", views.UserRegisterationAPIView.as_view(), name="create-user"),
    path("login2", views.my_view),
    path('getUsersByGroup/<specialty>', views.getUsersByGroup),
    # path('createUser', views.create),
    # path('deleteUser/<id>', views.destroy),
    # path('updateUser/<id>', views.update)

]
