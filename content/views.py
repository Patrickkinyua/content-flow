from django.shortcuts import render
from .serializers import ContentSerializers, TagSerializers
from .models import article, tag, ArticleLike
from rest_framework import viewsets
from .permissions import IsAuthor
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response




# Create your views here.
class ContentViewSet(viewsets.ModelViewSet):
    queryset = article.objects.all()
    serializer_class = ContentSerializers
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthor]
    
    

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def like(self, request, pk=None):
        obj = self.get_object()
        like, created = ArticleLike.objects.get_or_create(user=request.user, article=obj)
        if created:
            return Response({'status': 'liked'})
        return Response({'status': 'already liked'})

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def unlike(self, request, pk=None):
        obj = self.get_object()
        ArticleLike.objects.filter(user=request.user, article=obj).delete()
        return Response({'status': 'unliked'})
class TagViewSet(viewsets.ModelViewSet):
    queryset = tag.objects.all()
    serializer_class = TagSerializers
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthor]
