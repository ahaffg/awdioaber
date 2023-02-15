from django.contrib import admin
from .models import category

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'text'
        'blog_category',
        'image',
    )

    ordering = ('title',)

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Article)
admin.site.register(Blog_category)