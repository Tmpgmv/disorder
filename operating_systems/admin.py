from django.contrib import admin

from general.admin_mixin import ReadOnlyAdminMixin
from operating_systems.models import OperatingSystem


@admin.register(OperatingSystem)
class OperatingSystemAdmin(ReadOnlyAdminMixin,
                           admin.ModelAdmin):
    pass
