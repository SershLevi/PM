from django.contrib import admin

from .models import (
    Project,
    Task,
    Status,
    Brand)


class AddAdmin(admin.ModelAdmin):
    list_display = ['name']


class Add2Admin(admin.ModelAdmin):
    list_display = ['text']


class AddAdmin(admin.ModelAdmin):
    model = Project

    list_display = [
        'name',
    ]


admin.site.register(Task, AddAdmin)
admin.site.register(Status, AddAdmin)
# admin.site.register(Url, AddAdmin)
admin.site.register(Brand, AddAdmin)

admin.site.register(Project, AddAdmin)
