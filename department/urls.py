
from django.urls import path,include
from django import views
from department.views import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register('CustomeUser', CustomUserViewSet,basename="CustomeUser")
router.register('project/', projectViewSet,basename="project")


urlpatterns = [

    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),

]
