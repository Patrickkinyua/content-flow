from .models import article, tag
from rest_framework import serializers


class ContentSerializers(serializers.ModelSerializer):
    like_count = serializers.IntegerField(source='likes.count', read_only=True)
    liked = serializers.SerializerMethodField()

    class Meta:
        model = article
        # '__all__' will include model fields plus additional serializer fields defined above
        fields = '__all__'

    def get_liked(self, obj):
        request = self.context.get('request')
        user = getattr(request, 'user', None)
        if user and user.is_authenticated:
            return obj.likes.filter(user=user).exists()
        return False


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = tag
        fields = '__all__'