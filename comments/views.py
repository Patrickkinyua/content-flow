from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db.models import Prefetch
from .serializers import CommentSerializer
from .models import Comment
from .permissions import IsAuthorOrReadOnly

class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get_queryset(self):
        qs = Comment.objects.filter(
            is_deleted=False,
            parent=None
        ).select_related("author").prefetch_related(
            Prefetch("replies", queryset=Comment.objects.select_related("author"))
        )
        article_pk = self.kwargs.get("article_pk")
        if article_pk:
            qs = qs.filter(article_id=article_pk)
        return qs

    def perform_create(self, serializer):
        article_pk = self.kwargs.get("article_pk")
        serializer.save(author=self.request.user, article_id=article_pk)

    def perform_update(self, serializer):
        serializer.save(is_edited=True)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.content = "[deleted]"
        instance.save()