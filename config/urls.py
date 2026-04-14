from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from projects.views import ProjectViewSet
from tasks.views import TaskViewSet
from users.views import CookieTokenObtainPairView
from users.views import LogoutView


router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', CookieTokenObtainPairView.as_view()),
 path('api/logout/', LogoutView.as_view()),
]
