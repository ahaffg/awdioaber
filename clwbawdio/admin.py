from django.contrib import admin
from .models import Clwb

# Register your models here.


class ClwbAdmin(admin.ModelAdmin):
    list_display = (
        'month',
        'image',
        'title',
        'description',
    )

    ordering = ('month',)

admin.site.register(Clwb)
