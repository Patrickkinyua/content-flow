from django.urls import path, include
from rest_framework import routers
from .views import CommentViewSet

router = routers.DefaultRouter()
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    # Nested route: articles/<article_pk>/comments/
    path('articles/<int:article_pk>/', include(router.urls)),
]
