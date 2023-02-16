from django.contrib import admin
from .models import Category

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

class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(ArticleAdmin)
admin.site.register(Blog_category)
admin.site.register(BlogAdmin)