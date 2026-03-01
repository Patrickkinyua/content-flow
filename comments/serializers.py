from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    replies = serializers.SerializerMethodField()
    like_count = serializers.IntegerField(source='likes.count', read_only=True)
    liked = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            "id",
            "article",
            "author",
            "parent",
            "content",
            "is_edited",
            "created_at",
            "replies",
            "like_count",
            "liked",
        ]
        read_only_fields = ["author", "is_edited"]

    def get_replies(self, obj):
        replies = obj.replies.filter(is_deleted=False)
        return CommentSerializer(replies, many=True).data

    def get_liked(self, obj):
        request = self.context.get('request')
        user = getattr(request, 'user', None)
        if user and user.is_authenticated:
            return obj.likes.filter(user=user).exists()
        return False