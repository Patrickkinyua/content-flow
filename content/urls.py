from .views import ContentViewSet, TagViewSet
from rest_framework import routers
from django.urls import path, include
router = routers.DefaultRouter()
router.register(r'content', ContentViewSet)
router.register(r'tag', TagViewSet)
urlpatterns = [
    path('', include(router.urls)), 
]