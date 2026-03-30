from django.contrib import admin

from general.admin_mixin import ReadOnlyAdminMixin
from infrastructure.models import ItemInInfrastructureList


@admin.register(ItemInInfrastructureList)
class ItemInInfrastructureListAdmin(ReadOnlyAdminMixin,
                   admin.ModelAdmin):
    pass
