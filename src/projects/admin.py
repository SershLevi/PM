from django.contrib import admin
from protector.admin import PermissionOwnerInline

from .models import (
    Project,
    Task,
    Status,
)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name']


class TaskAdmin(admin.ModelAdmin):
    list_display = ['name']


class StatusAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Task, TaskAdmin)
admin.site.register(Status, StatusAdmin)


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
