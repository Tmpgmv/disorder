from django.contrib import admin

from general.admin_mixin import ReadOnlyAdminMixin
from .models import EducationalFacility


@admin.register(EducationalFacility)
class EducationalFacilityAdmin(ReadOnlyAdminMixin,
                               admin.ModelAdmin):
    pass

