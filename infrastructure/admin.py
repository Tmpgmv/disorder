from django.contrib import admin

from general.admin_mixin import ReadOnlyAdminMixin
from infrastructure.models import InfrastructureListForAdmin, InfrastructureListForPassport


@admin.register(InfrastructureListForPassport)
class ItemInInfrastructureListAdmin(ReadOnlyAdminMixin,
                   admin.ModelAdmin):
    pass

@admin.register(InfrastructureListForAdmin)
class InfrastructureListForAdminAdmin(ReadOnlyAdminMixin,
                   admin.ModelAdmin):
    pass
