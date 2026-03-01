from django.contrib import admin
from .models import article, tag, ArticleLike

# Register your models here.

admin.site.register(article)
admin.site.register(tag)
admin.site.register(ArticleLike)
