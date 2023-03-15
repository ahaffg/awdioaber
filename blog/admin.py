from django.contrib import admin
from .models import Blog, Category

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'title',
        'description',
        'content',
        'date',
        'author',
        'image'
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Blog)
admin.site.register(Category)
