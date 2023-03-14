from django.contrib import admin

from .models import Blog, BlogComment, BlogView, Like, Category


class BlogListAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured', 'author',
                    'category',)
    list_filter = ('author',
                   'category',)

    list_editable = ('featured',)


admin.site.register(Blog,  BlogListAdmin)
admin.site.register(Category)
admin.site.register(BlogComment)
admin.site.register(BlogView)
admin.site.register(Like)