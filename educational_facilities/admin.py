from django.contrib import admin

from courses.models import CoursesInFacilities
from general.admin_mixin import ReadOnlyAdminMixin
from .models import EducationalFacility


@admin.register(EducationalFacility)
class EducationalFacilityAdmin(ReadOnlyAdminMixin,
                               admin.ModelAdmin):
    pass


@admin.register(CoursesInFacilities)
class CoursesInFacilitiesAdmin(ReadOnlyAdminMixin,
                               admin.ModelAdmin):
    pass
