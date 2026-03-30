from django.contrib import admin

from general.admin_mixin import ReadOnlyAdminMixin
from tasks.models import TaskGroup, Task, TaskAuthor, Distortable, Script, PrintableTask


@admin.register(TaskGroup)
class TaskGroupAdmin(ReadOnlyAdminMixin,
                     admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(ReadOnlyAdminMixin,
                admin.ModelAdmin):
    pass


@admin.register(TaskAuthor)
class TaskAuthorAdmin(ReadOnlyAdminMixin,
                      admin.ModelAdmin):
    raw_id_fields = ('task',)


@admin.register(Distortable)
class DistortableAdmin(ReadOnlyAdminMixin,
                       admin.ModelAdmin):
    raw_id_fields = ('task',)


@admin.register(Script)
class ScriptAdmin(ReadOnlyAdminMixin,
                  admin.ModelAdmin):
    raw_id_fields = ('task',)


@admin.register(PrintableTask)
class PrintableTaskAdmin(ReadOnlyAdminMixin,
                         admin.ModelAdmin):
    raw_id_fields = ('task',)
