from django.urls import path, include
from rest_framework import routers
from posts.views import PostViewSet

router = routers.DefaultRouter()
router.register(r'blog', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]