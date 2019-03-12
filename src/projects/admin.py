from django.contrib import admin
from protector.admin import PermissionOwnerInline

from .models import (
    Project,
    Task,
    Status,
    Url)


class AddAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Task, AddAdmin)
admin.site.register(Status, AddAdmin)
admin.site.register(Url, AddAdmin)


class ProjectsAdmin(admin.ModelAdmin):
    model = Project

    list_display = [
        'name',
        'get_absolute_url',
        'project_manager',
        'project_status',
    ]

    list_filter = (
    )

    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ()



admin.site.register(Project, ProjectsAdmin)
