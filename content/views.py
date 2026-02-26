from django.shortcuts import render
from .serializers import ContentSerializers, TagSerializers
from .models import article, tag
from rest_framework import viewsets




# Create your views here.
class ContentViewSet(viewsets.ModelViewSet):
    queryset = article.objects.all()
    serializer_class = ContentSerializers

    def perform_create(self, serializer):
        serializer.save()
class TagViewSet(viewsets.ModelViewSet):
    queryset = tag.objects.all()
    serializer_class = TagSerializers