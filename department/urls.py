
from django.urls import path,include
from django import views
from department.views import RegisterView,LoginView,CustomUserViewSet,ProjectViewSet,ResetPasswordEmailRequestSerializer
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()

router.register('CustomeUser', CustomUserViewSet,basename="CustomeUser")
router.register('project/', ProjectViewSet,basename="project")


urlpatterns = [

    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


]
