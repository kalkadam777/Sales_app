from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from . import views
from django.contrib.auth.views import LogoutView


router = DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
 