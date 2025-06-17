from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'timestamp', 'updated', 'published']
    search_fields = ['id', 'title', 'content', 'published']
    
admin.site.register(Article, ArticleAdmin)

# Register your models here.
