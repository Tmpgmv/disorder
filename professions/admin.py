from django.contrib import admin

from general.admin_mixin import ReadOnlyAdminMixin
from professions.models import Profession


@admin.register(Profession)
class EducationalFacilityAdmin(ReadOnlyAdminMixin,
                               admin.ModelAdmin):
    pass
