from django.conf import settings
from django.db import models
from django.utils import timezone

class Comment(models.Model):
    article = models.ForeignKey(
        "content.article",
        on_delete=models.CASCADE,
        related_name="comments",
        db_index=True
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="replies"
    )

    content = models.TextField()

    is_edited = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(default=timezone.now, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["article", "created_at"]),
        ]

    def __str__(self):
        return f"{self.author} on {self.article}"