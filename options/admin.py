from django.contrib import admin

from options.models import Options


class OptionsAdmin(admin.ModelAdmin):
    def has_add_permission(self, *args, **kwargs):
        return not Options.objects.exists()
    exclude = []

admin.site.register(Options, OptionsAdmin)