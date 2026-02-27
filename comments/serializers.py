from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    replies = serializers.SerializerMethodField()

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
        ]
        read_only_fields = ["author", "is_edited"]

    def get_replies(self, obj):
        replies = obj.replies.filter(is_deleted=False)
        return CommentSerializer(replies, many=True).data