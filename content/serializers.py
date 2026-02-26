from .models import article, tag
from rest_framework import serializers




class ContentSerializers(serializers.ModelSerializer):
    class Meta:
        model= article
        fields = '__all__'
class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model= tag
        fields = '__all__'