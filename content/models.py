from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField




class tag(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    


class article(models.Model):
    STATUS_CHOICES = [("draft", "Draft"),("published","Published")]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,default="draft")
    title = models.CharField(max_length=200)
    body = models.TextField()
    image= CloudinaryField('image', blank=True, null=True)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tags = models.ManyToManyField(tag, related_name="articles", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.title} by {self.author}"


    


class ArticleLike(models.Model):
    """A record that a user liked an article."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="article_likes"
    )
    article = models.ForeignKey(
        article,
        on_delete=models.CASCADE,
        related_name="likes"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "article")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user} likes {self.article}"

    
