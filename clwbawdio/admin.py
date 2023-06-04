from django.contrib import admin
from .models import Clwb, Category

# Register your models here.


class ClwbAdmin(admin.ModelAdmin):
    list_display = (
        'month',
        'image',
        'title',
        'description',
        'category',
    )

    ordering = ('month',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Category)
admin.site.register(Clwb)
