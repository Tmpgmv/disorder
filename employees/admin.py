from django.contrib import admin

from employees.models import Employee
from general.admin_mixin import ReadOnlyAdminMixin


@admin.register(Employee)
class EducationalFacilityAdmin(ReadOnlyAdminMixin,
                               admin.ModelAdmin):
    pass

