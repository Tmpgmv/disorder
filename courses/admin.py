from django.contrib import admin

from courses.models import Course
from general.admin_mixin import ReadOnlyAdminMixin


@admin.register(Course)
class EducationalFacilityAdmin(ReadOnlyAdminMixin,
                               admin.ModelAdmin):
    pass
