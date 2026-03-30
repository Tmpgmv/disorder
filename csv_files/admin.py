from django.contrib import admin

from csv_files.models import CsvFile, DistortableInCsv
from general.admin_mixin import ReadOnlyAdminMixin


class DistortableInCsvInline(admin.StackedInline):
    model = DistortableInCsv
    extra = 0


@admin.register(CsvFile)
class CsvFileAdmin(ReadOnlyAdminMixin,
                   admin.ModelAdmin):
    raw_id_fields = ('task',)
    inlines = [DistortableInCsvInline, ]
