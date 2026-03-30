from django.contrib import admin

from general.admin_mixin import ReadOnlyAdminMixin
from images.models import Img


@admin.register(Img)
class ImgAdmin(ReadOnlyAdminMixin,
               admin.ModelAdmin):
    raw_id_fields = ('task',)
