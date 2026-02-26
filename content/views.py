from django.shortcuts import render
from .serializers import ContentSerializers, TagSerializers
from .models import article, tag
from rest_framework import viewsets
from .permissions import IsAuthor
from rest_framework.permissions import IsAuthenticatedOrReadOnly




# Create your views here.
class ContentViewSet(viewsets.ModelViewSet):
    queryset = article.objects.all()
    serializer_class = ContentSerializers
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthor]
    

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
class TagViewSet(viewsets.ModelViewSet):
    queryset = tag.objects.all()
    serializer_class = TagSerializers
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthor]