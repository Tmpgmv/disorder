from django.contrib import admin

from files.models import File
from general.admin_mixin import ReadOnlyAdminMixin


@admin.register(File)
class FileAdmin(ReadOnlyAdminMixin,
                   admin.ModelAdmin):
    raw_id_fields = ('task',)


