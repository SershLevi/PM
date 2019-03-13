from django.contrib import admin
from protector.admin import PermissionOwnerInline

from .models import (
    Project,
    Task,
    Status,
    Url, Brand, Message)


class AddAdmin(admin.ModelAdmin):
    list_display = ['name']

class Add2Admin(admin.ModelAdmin):
    list_display = ['text']


admin.site.register(Task, AddAdmin)
admin.site.register(Status, AddAdmin)
# admin.site.register(Url, AddAdmin)
admin.site.register(Brand, AddAdmin)
admin.site.register(Message, Add2Admin)


class ProjectsAdmin(admin.ModelAdmin):
    model = Project

    list_display = [
        'name',
        'get_absolute_url',
        'manager',
        'status',
    ]

    list_filter = (
    )

    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ()



admin.site.register(Project, ProjectsAdmin)
