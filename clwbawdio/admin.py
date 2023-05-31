from django.contrib import admin
from .models import Clwb

# Register your models here.


class ClwbAdmin(admin.ModelAdmin):
    list_display = (
        'month',
        'name',
        'image',
        'description',
        'date',
    )

    ordering = ('date',)

admin.site.register(Clwb)
